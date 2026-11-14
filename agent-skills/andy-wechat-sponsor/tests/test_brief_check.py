import importlib.util
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("sponsor_brief_check", HERE / "scripts/brief_check.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class BriefCheckTests(unittest.TestCase):
    def load_template(self):
        return json.loads((HERE / "templates/brand-brief.json").read_text(encoding="utf-8"))

    def test_blank_template_needs_evidence(self):
        self.assertEqual(mod.inspect_brief(self.load_template())["status"], "NEEDS_EVIDENCE")

    def test_paid_without_label_blocked(self):
        d = self.load_template()
        d["cooperation"]["ad_label_plan"] = "unknown"
        self.assertEqual(mod.inspect_brief(d)["status"], "BLOCKED")

    def test_unverified_true_claim_missing_source_is_blocked(self):
        d = self.load_template()
        d["evidence"] = [{"claim": "功能 A 可用", "verified": True}]
        self.assertEqual(mod.inspect_brief(d)["status"], "BLOCKED")

    def test_complete_brief_passes_structural_gate(self):
        d = self.load_template()
        d["brand"].update(name="模拟公司", legal_entity="模拟主体", official_url="https://example.org", verified=True)
        d["product"].update(name="模拟产品", official_url="https://example.org/products")
        d.update(target_reader="团队文档负责人", reader_problem="检索困难", campaign_goal="认知沟通", author_approved=True)
        d["evidence"] = [{"claim":"公开规格", "source":"https://example.org/spec", "verified_at":"2026-11-14", "verified":True}]
        d["cooperation"]["permission_to_publish"] = True
        self.assertEqual(mod.inspect_brief(d)["status"], "READY")

if __name__ == "__main__":
    unittest.main()
