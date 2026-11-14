#!/usr/bin/env python3
"""Offline, read-only intake gate for Andy WeChat Sponsor Skill. Python 3.10+ stdlib."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

MISSING = (None, "", "unknown", "待确认", "待提供", "tbd")


def has_value(value: object) -> bool:
    return isinstance(value, str) and value.strip().lower() not in MISSING


def inspect_brief(data: dict) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    brand = data.get("brand") if isinstance(data.get("brand"), dict) else {}
    product = data.get("product") if isinstance(data.get("product"), dict) else {}
    cooperation = data.get("cooperation") if isinstance(data.get("cooperation"), dict) else {}

    for key, value in (
        ("brand.name", brand.get("name")),
        ("brand.legal_entity", brand.get("legal_entity")),
        ("brand.official_url", brand.get("official_url")),
        ("product.name", product.get("name")),
        ("product.official_url", product.get("official_url")),
        ("target_reader", data.get("target_reader")),
        ("reader_problem", data.get("reader_problem")),
        ("campaign_goal", data.get("campaign_goal")),
    ):
        if not has_value(value):
            warnings.append(f"missing: {key}")

    if brand.get("verified") is not True:
        warnings.append("brand legal identity has not been verified")
    if not isinstance(data.get("deliverables"), list) or not data["deliverables"]:
        warnings.append("deliverables not defined")
    evidence = data.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        warnings.append("no claim-level evidence; draft cannot assert product results")
    else:
        for index, item in enumerate(evidence):
            if not isinstance(item, dict) or not has_value(item.get("claim")):
                errors.append(f"invalid evidence item {index}: missing claim")
                continue
            if item.get("verified") is True and not (
                has_value(item.get("source")) and has_value(item.get("verified_at"))
            ):
                errors.append(f"invalid verified evidence item {index}: needs source and date")
            if item.get("verified") is not True:
                warnings.append(f"unverified claim {index}: must be omitted or explicitly attributed")
    if cooperation.get("paid") is True and not has_value(cooperation.get("ad_label_plan")):
        errors.append("paid cooperation requires an explicit advertising disclosure plan")
    elif cooperation.get("paid") is True and "广告" not in str(cooperation.get("ad_label_plan")):
        warnings.append("ad_label_plan should include conspicuous 广告 label if applicable")
    if data.get("author_approved") is not True:
        warnings.append("author has not approved publication")
    if cooperation.get("permission_to_publish") is not True:
        warnings.append("publishing permission not granted")

    state = "BLOCKED" if errors else ("NEEDS_EVIDENCE" if warnings else "READY")
    return {"status": state, "errors": errors, "warnings": warnings,
            "reminder": "Read-only checklist, not legal clearance or permission to publish."}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a PRIVATE sponsor brief without network or writes")
    parser.add_argument("brief", help="Local JSON brief path")
    args = parser.parse_args(argv)
    try:
        raw = Path(args.brief).read_text(encoding="utf-8")
        obj = json.loads(raw)
        if not isinstance(obj, dict):
            raise ValueError("Brief root must be a JSON object")
        out = inspect_brief(obj)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "INPUT_ERROR", "error": str(exc)}, ensure_ascii=False), file=sys.stdout)
        return 2
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 1 if out["status"] == "BLOCKED" else 0


if __name__ == "__main__":
    raise SystemExit(main())
