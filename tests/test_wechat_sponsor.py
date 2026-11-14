import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import router


class SponsorIntegrationTests(unittest.TestCase):
    def test_only_sponsored_wechat_goes_to_sponsor(self):
        for task in [
            "帮我处理一份公众号商单 Brief，定选题和报价",
            "拿这份品牌 Brief 写一篇公众号软植入商单",
            "公众号品牌合作需要报价与交付验收",
        ]:
            self.assertEqual(router.route(task)["scenario"], "wechat_sponsor", task)
        self.assertEqual(router.route("写一篇普通微信公众号文章")["scenario"], "wechat")

    def test_spread_to_other_platform_not_hijacked(self):
        self.assertEqual(router.route("将公众号商单改为 Threads 短帖", "threads")["scenario"], "threads")

    def test_audit_keeps_compliance_route(self):
        self.assertEqual(router.route("只审核这个公众号商单是否违规")["scenario"], "compliance")

    def test_sponsor_prompt_contains_relevant_rules(self):
        sel = router.route("帮我写一篇公众号商单")
        prompt = router.compose_prompt("帮我写一篇公众号商单", sel)
        self.assertIn("广告识别", prompt)
        self.assertIn("显著", prompt)
        self.assertIn("BLOCKED", prompt)
        self.assertIn("BUNDLED PINNED TEXT LOADED", prompt)

    def test_prompt_is_read_only_without_keys(self):
        sel = router.route("公众号商单报价")
        prompt = router.compose_prompt("公众号商单报价", sel)
        self.assertNotIn("OPENAI_API_KEY=", prompt)
        self.assertIn("不自动", prompt)

if __name__ == "__main__":
    unittest.main()
