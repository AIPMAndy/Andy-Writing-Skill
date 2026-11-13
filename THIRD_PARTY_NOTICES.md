# Third-party notices

This project includes pinned, unmodified snapshots of two official writing resources by 数字生命卡兹克 / KKKKhazix. Their MIT license notices are preserved in each vendor directory. Andy's routing and integration rules are maintained separately; this integration is not an endorsement by the upstream author.

| Module | Source | Pinned commit | License |
|---|---|---|---|
| khazix-writer | https://github.com/KKKKhazix/khazix-skills/tree/71cd50ffe1f1f4d400b54be967dc6b59379aff8f/khazix-writer | 71cd50ffe1f1f4d400b54be967dc6b59379aff8f | vendor/khazix-writer/LICENSE |
| human-writing 1.2.0 | https://github.com/KKKKhazix/human-writing/tree/a4ed3735e61ae63fd454df253ebecb0916b3a146/human-writing | a4ed3735e61ae63fd454df253ebecb0916b3a146 | vendor/human-writing/LICENSE |

Retrieved and verified on 2026-11-13 (Asia/Shanghai). Each imported file is listed with its original Git blob SHA and SHA-256 in `vendor/manifest.json`.

The Khazix style examples are instructional examples, never evidence of the user's experience. Ordinary articles and other works linked from upstream repositories are not automatically covered by these software licenses.

Other external modules in `catalog.json` remain source-linked adapters; they are not downloaded or executed automatically.

## Update procedure

Read the source changes, verify the license, pin a new commit, replace the corresponding complete vendor files, regenerate the manifest from those verified files, and run the relevant checks. Do not auto-update to an unreviewed branch head.
