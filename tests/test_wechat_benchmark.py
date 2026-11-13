import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import router


class WechatBenchmarkTests(unittest.TestCase):
    def test_wechat_uses_one_primary_writer_and_one_editor(self):
        selection = router.route('写一篇公众号长文，介绍我的开源项目，引导咨询服务，最后去 AI 味')
        self.assertEqual(selection['scenario'], 'wechat')
        self.assertEqual(selection['pipeline'][:2], ['khazix-writer', 'human-writing'])
        self.assertNotIn('copywriting', selection['pipeline'])
        self.assertNotIn('humanizer', selection['pipeline'])

    def test_longform_medium_wins_over_cold_knowledge_angle(self):
        self.assertEqual(router.route('写一篇公众号长文，说个冷知识，介绍免费开源项目')['scenario'], 'wechat')

    def test_named_benchmark_and_rewrite(self):
        for task in ['按卡兹克风格写一篇长文', '把这篇公众号文章改成卡兹克风格']:
            self.assertEqual(router.route(task)['scenario'], 'wechat')

    def test_short_content_keeps_its_medium(self):
        self.assertEqual(router.route('按卡兹克风格写一条 Threads 短帖')['scenario'], 'threads')
        self.assertEqual(router.route('卡兹克风格，写一个口播逐字稿')['scenario'], 'video_script')

    def test_composed_prompt_contains_actual_upstream_and_overlay(self):
        text = router.compose_prompt('写一篇公众号长文', router.route('写一篇公众号长文'))
        self.assertIn('BUNDLED PINNED TEXT LOADED', text)
        self.assertIn('调查实验型', text)
        self.assertIn('活人感写作 1.2.0', text)
        self.assertIn('references/style_examples.md', text)
        self.assertIn('references/reality.md', text)
        self.assertIn((ROOT/'references/wechat-standard.md').read_text(encoding='utf-8'), text)
        self.assertNotIn('vendor/human-writing/scripts/check_prose.py\n#!/usr/bin', text)

    def test_other_scenarios_do_not_load_longform_text(self):
        text = router.compose_prompt('写一条 Threads 短帖', router.route('写一条 Threads 短帖'))
        self.assertNotIn('活人感写作 1.2.0', text)

    def test_all_snapshot_files_match_the_pinned_blobs(self):
        manifest = json.loads((ROOT/'vendor/manifest.json').read_text(encoding='utf-8'))
        for path, item in manifest['files'].items():
            data = (ROOT/path).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), item['sha256'], path)
            self.assertEqual(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(), item['git_blob_sha'], path)

    def test_missing_or_changed_bundle_fails_visibly(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root/'vendor').mkdir()
            relative = 'vendor/example.md'
            (root/relative).write_text('changed', encoding='utf-8')
            manifest = {'files': {relative: {'sha256': hashlib.sha256(b'expected').hexdigest()}}}
            (root/'vendor/manifest.json').write_text(json.dumps(manifest), encoding='utf-8')
            with patch.object(router, 'ROOT', root), patch.object(router, 'THIRD', {'sample': {'bundled_files': [relative]}}):
                with self.assertRaisesRegex(RuntimeError, 'verification failed'):
                    router.load_bundled_skills(['sample'])
                (root/relative).unlink()
                with self.assertRaisesRegex(RuntimeError, 'unavailable'):
                    router.load_bundled_skills(['sample'])

    def test_bundled_loader_rejects_outside_paths(self):
        with patch.object(router, 'THIRD', {'sample': {'bundled_files': ['../outside.md']}}):
            with self.assertRaisesRegex(RuntimeError, 'Unapproved'):
                router.load_bundled_skills(['sample'])


if __name__ == '__main__':
    unittest.main()
