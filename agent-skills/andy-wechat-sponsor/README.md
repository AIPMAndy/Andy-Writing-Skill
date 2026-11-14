# Andy WeChat Sponsor Skill｜AI 酋长 Andy 公众号商单闭环

面向公众号品牌合作，从 **询单 → 筛选 → 报价 → 选题 → 实测 → 写稿 → 合规 → 交付 → 数据复盘 → 复购** 的专属 Agent Skill。不是“提示词合集”，也不保证月入十万或商单成交。

## 安装（独立 Skill）

将本目录 `agent-skills/andy-wechat-sponsor` 复制或软链到 Agent 的 Skills 目录即可：

```bash
git clone https://github.com/AIPMAndy/Andy-Writing-Skill.git
mkdir -p ~/.codex/skills ~/.claude/skills
ln -s "$(pwd)/Andy-Writing-Skill/agent-skills/andy-wechat-sponsor" ~/.codex/skills/andy-wechat-sponsor
# 使用 Claude Code 时也可以链接到 ~/.claude/skills/andy-wechat-sponsor
```

**在 ChatGPT 对话中**，打开此仓库的 `SKILL.md` 或上传本目录作为参考，让助手按步骤执行；仅分享 GitHub 链接**不等于 ChatGPT 自动安装**。

**与主路由联动（可选）**：

```bash
cd Andy-Writing-Skill
python3 scripts/router.py route --text '帮我处理一份公众号商单 Brief，定选题和报价'
python3 scripts/router.py prompt --text '做公众号品牌合作，给商单交付包' > sponsor-prompt.md
```

## 五种工作模式

| 说什么 | 交付什么 |
|---|---|
| “做我的公众号招商媒体包” | 媒体包/价值定位/证据缺口 |
| “品牌来问报价” | 商单评估/报价结构/回复文案/合同风险 |
| “拿这份 Brief 写公众号商单” | 选题卡/正文/广告标识/素材取证/交付包 |
| “审核品牌修改意见” | 逐项风险/接受与拒绝理由/合规改稿 |
| “复盘这条商单” | 履约与阅读/商业效果（分口径）/复购建议 |

## 私有 Brief 先检查

```bash
cp agent-skills/andy-wechat-sponsor/templates/brand-brief.json /tmp/private-brief.json
python3 agent-skills/andy-wechat-sponsor/scripts/brief_check.py /tmp/private-brief.json
```

`NEEDS_EVIDENCE` 表示还缺资料；`BLOCKED` 是明确红线；`READY` 仅表示字段和证据门槛通过，**不代表获得发布授权、商单合法或效果有保障**。生产项目请在本地私有目录填写，不把 Brief 上传公有仓库。零第三方 Python 依赖。

## 专属组合

- **Andy-Writing-Skill**：公众号长文主笔和文章事实检查；商单时保持广告合规优先。
- **MDskill-Web**：公众号排版与可预览 HTML，需实际导出后才能声称完成。
- **Andy-Content-Checker**：编辑层面风险提醒，不能替代法律或平台审核。

## 信息来源与边界

灵感源：[西堂的 X 文章《AI公众号稳定月入变现10万+，从选题到接商单的万字实操教程》](https://x.com/xitang_ai/status/2121207382630117537)。2026-11-14 可核验该标题和外部转发，**文章全文无法稳定抓取**；此目录为 Andy 专属原创业务工作流，不声称逐条复现原帖方法，作者收益亦未独立审计。

广告识别与真实性核对依据国家市场监管总局《互联网广告管理办法》及其《互联网广告可识别性执法指南》，见 `references/compliance.md`。

作者：[AI 酋长 Andy](https://github.com/AIPMAndy) · [官网](https://metaver.vip/) · 公开联系微信 `AIPMAndy`。开源沿用主仓库 MIT 许可（具体以上游 LICENSE 为准）。
