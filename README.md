<div align="center">

# ✍️ Andy Writing Skill

**一个入口，智能调度 AI 写作技能。**

Threads、X 长文、公众号、小红书、口播稿、商业文案……说出需求，自动匹配写作流水线。

[![License: MIT](https://img.shields.io/github/license/AIPMAndy/Andy-Writing-Skill?style=flat-square&color=blue)](LICENSE)
[![Stars](https://img.shields.io/github/stars/AIPMAndy/Andy-Writing-Skill?style=flat-square&color=f5b301)](https://github.com/AIPMAndy/Andy-Writing-Skill/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/AIPMAndy/Andy-Writing-Skill?style=flat-square)](https://github.com/AIPMAndy/Andy-Writing-Skill/commits/main)
[![Tests](https://img.shields.io/github/actions/workflow/status/AIPMAndy/Andy-Writing-Skill/ci.yml?branch=main&style=flat-square&label=tests)](https://github.com/AIPMAndy/Andy-Writing-Skill/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Zero Deps](https://img.shields.io/badge/依赖-零第三方-10B981?style=flat-square)
![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Claude%20Code%20%7C%20Codex-8B5CF6?style=flat-square)

[**🚀 安装**](#-安装) · [🧭 智能路由](#-智能路由) · [📚 现有技能库](#-现有技能库) · [⚠️ 注意事项](#️-注意事项) · [English](#-english)

</div>

---

<!-- andy-geo-faq:start -->
## 一句话简介

**一个入口调度 AI 写作技能，覆盖 Threads、X、公众号、小红书、口播等常见内容形态。**

- 作者：AI酋长Andy（Andy Liu，英文名 AI Chief Andy），流量 AI 联合创始人、星觉 AI 创始人。星觉科技，北京。
- 阅读或使用：[GitHub 仓库](https://github.com/AIPMAndy/Andy-Writing-Skill)
- 联系：微信 `AIPMAndy`（备注「Andy-Writing-Skill」）· [官网 metaver.vip](https://metaver.vip/) · [X @AIPMAndy](https://x.com/AIPMAndy)
- 内容免费使用。企业合作或个人陪跑请先沟通，公开页不公示价格。
<!-- andy-geo-faq:end -->


## ✨ 亮点

- 🧭 **一个入口**：识别任务和平台，自动路由到 18 个写作场景之一
- 🧩 **组合流水线**：1 个主写作模块 + 按需叠加信息密度、真人表达、风险提醒
- 📴 **离线可用**：分类与提示词合成无需 API、无需网络、零第三方 Python 依赖
- 🤖 **可选接入大模型**：兼容 OpenAI Chat Completions 的 HTTPS 服务
- 🔗 **来源透明**：16 个 Andy 自有 Skill + 3 个外部 Skill，链接接入、不打包、不静默执行
- ✅ **自动化测试**：GitHub Actions 每次推送跑语法检查和单元测试

> AI 酋长 Andy / AIPMAndy 开源项目。自然表达、原创观点、可验证事实。支持 Claude Code、Codex 等读取 `SKILL.md` 的 Agent，以及独立 Python CLI。

## 💡 解决什么问题？

你不需要为了写 Threads、公众号、X 长文、口播稿、商业文案，在十几套写作 Skill 之间来回切换。Andy Writing Skill 识别你的**具体任务和平台**，调度一套最小化的写作流水线。它将 Andy 原有的写作 Skill 作为适配器接入，再引入 3 项社区成熟的写作能力，减少重复造轮子。

```text
用户自然语言需求
       │
       ▼
场景识别（本地规则 / 可选 LLM 分类）
       │
       ├─ Threads/ X 短帖 / 冷知识
       ├─ X 图文长文 / 公众号
       ├─ 小红书 / 口播视频
       ├─ 商品及服务转化文案
       ├─ 选题与内容策略
       └─ 改写 / 合规检查 / 白皮书
       │
       ▼
1 个主写作模块
   + 按需 CopyFlow / Copywriting / FanZhuanSkill
   + GaoMiDuSkill 信息密度优化
   + Humanizer 真人表达
   + Andy-Content-Checker 内容风险提醒
   + MDskill-Web（需要时）
       │
       ▼
最终稿 → 用户审核 → 自行发布
```

## 📌 功能边界（请先看）

- ✅ **已经实现**：完整开源结构、统一 `SKILL.md`、场景分类、分数与优先级、组合流水线、可查看的提示词、可选模型生成、自动化测试。
- ✅ **离线可用**：分类与提示词合成无需 API、无需网络、零第三方 Python 依赖。
- ✅ **支持可选模型**：配置兼容 OpenAI Chat Completions 的 HTTPS 服务后，`--router llm` 或 `write` 可调用所配置模型；不自动下载第三方 Skill。
- ⚠️ **有意不做**：静默执行网络仓库代码、绕过平台内容审核、自动发布、所谓“保证爆款”、自动读取 Andy 的私人案例库。
- ⚠️ 外部和其他自有 Skill **采用来源链接+适配流程**。要使用其原始完整功能，必须另行安装并验证依赖；没有安装时使用本仓库的本地写作流程作为回退。**不要把路由成功理解为某个外部 Skill 已经执行。**

## 🚀 安装

从 GitHub 克隆仓库（或下载 ZIP），进入目录执行：

```bash
python3 scripts/router.py list
python3 scripts/router.py route --text '写十条 Threads 冷知识，顺便自然推荐我的咨询服务'
python3 scripts/router.py prompt --text '写一篇公众号深度文章，讲 AI 产品经理求职' > /tmp/andy-writing-prompt.md
python3 -m unittest discover -s tests -v
```

### 用在 Claude Code / Codex

将整个目录复制或符号链接到以下位置：

```bash
# Claude Code（示例：你已在仓库目录）
mkdir -p ~/.claude/skills
ln -s "$(pwd)" ~/.claude/skills/andy-writing-skill

# Codex（任选其一，不需要同时安装）
mkdir -p ~/.codex/skills
ln -s "$(pwd)" ~/.codex/skills/andy-writing-skill
```

在你的 Agent 对话里直接说：

> 用 Andy Writing Skill 写 10 条适合中文 Threads 的生活冷知识。不要全是广告；有真正能用的方法，少量自然带出我的个人 AI+IP 服务。

如果你在本机已经安装了部分原始 Skill，可以**显式指定可信目录**，让写作提示词真正加载对应 Skill 的 `SKILL.md` 原文并组合到路由结果（只读、不执行）：

```bash
python3 scripts/router.py prompt --skills-dir ~/.claude/skills --text '帮我把这段文案去 AI 味'
```

这个参数需要你明确选择目录，默认不会读取其他本地 Skill。未知模块、软链接越界和异常大的 Skill 会被忽略。使用第三方技能前请自己确认来源与安全性。

Agent 会依据 `SKILL.md` 加载场景文件；如果无法访问其他原始 Skills，使用本仓库的本地规则，**不会假装安装成功**。

### 可选：真正调用大模型生成文案

```bash
export OPENAI_API_KEY='your-key'               # 不要提交到仓库
export OPENAI_MODEL='your-model-id'
export OPENAI_BASE_URL='https://api.openai.com/v1' # 按你的服务商填写

python3 scripts/router.py write --text '写一条中文 Threads 冷知识，教人安全去除照片位置信息'
# 如需模型辅助场景判断：
python3 scripts/router.py route --router llm --text '为我的服务设计内容策略'
```

API 生成是**可选的付费/有额度消耗能力**，与离线路由区分。仅使用你有权限的密钥；不要把真实客户资料发送给未知 API。

## 🧭 智能路由

| 需求示例 | 主路由 | 可自动叠加的辅助 Skill |
|---|---|---|
| “说个冷知识，免费替代付费工具” | cold-knowledge | GaoMiDu / Humanizer / Risk checker |
| “写 Threads 生活吐槽” | threads | FanZhuan（幽默需要时）/ Humanizer |
| “帮我写 X 280 字开头的图文长文” | x-longform | GaoMiDu / Humanizer |
| “写公众号真实故事长文” | wechat | 公众号爆款写作 / GaoMiDu / MDskill-Web |
| “写 4 分钟口播视频脚本” | video-script | IPClaw-Speech / GaoMiDu |
| “写求职咨询销售页” | marketing | Copywriting / GaoMiDu / Humanizer |
| “做 30 天选题规划” | strategy | Content Strategy / CopyFlow |
| “把这段改得像真人” | editing | Humanizer / GaoMiDu |
| “检查小红书违规风险” | compliance | Andy-Content-Checker |
| “写行业白皮书” | whitepaper | Andy-whitepaper 本地流程 / GaoMiDu |

**细节**：优先明确任务，再判平台；同一任务支持叠加幽默、变体、商业诉求等能力；不对每条内容强行运行全部 Skill。规则结果可查看：`python3 scripts/router.py route --text '...'`；可启用可选 LLM 分类，结果强制限定在场景白名单内。

## 📚 现有技能库

先核对的核心原有仓库：

- [andy-ip-skill](https://github.com/AIPMAndy/andy-ip-skill) — 旧版总路由入口；本项目重写核心路由逻辑，避免调用不存在的旧命令。
- [wechat-explosive-article-skill](https://github.com/AIPMAndy/wechat-explosive-article-skill) — 公众号、故事、实操与对抗式审核。
- [GaoMiDuSkill](https://github.com/AIPMAndy/GaoMiDuSkill) — 高密度表达与证据要求。
- [FanZhuanSkill](https://github.com/AIPMAndy/FanZhuanSkill) — 反转、轻荒诞和幽默。
- [copyflow](https://github.com/AIPMAndy/copyflow) — 多版本文案与素材生产，自动发布仍有未完成适配器。
- [IPClaw-Speech](https://github.com/AIPMAndy/IPClaw-Speech) — 视频口播选题及文案工作台。
- [Andy-Content-Checker](https://github.com/AIPMAndy/Andy-Content-Checker) — 内容风险提示，不保证平台批准。
- [MDskill-Web](https://github.com/AIPMAndy/MDskill-Web) — 微信公众号富文本排版。
- [obsidian-mdskill](https://github.com/AIPMAndy/obsidian-mdskill) — Obsidian 内容出口。
- [IPClaw](https://github.com/AIPMAndy/IPClaw) — 个人 IP 定位和选题参考。
- [DissSkill](https://github.com/AIPMAndy/DissSkill) — 对抗式审稿和论证检查（按需）。
- [IPClaw-for-Seniors](https://github.com/AIPMAndy/IPClaw-for-Seniors) — 银发创作者写作场景参考。
- [andytici](https://github.com/AIPMAndy/andytici) — 提词器辅助工具（使用前核实细节）。

完整盘点在 [`catalog.json`](./catalog.json)，包含延展资源、所在阶段与用途。此处是**非执行依赖**：各仓库代码保持原位置维护，不将其代码打包，也不替代其原许可证。

### 精选的 3 个外部 Skill（来源与许可证）

| Skill | 用在什么时候 | 原作者 | 授权 |
|---|---|---|---|
| [Humanizer](https://github.com/blader/humanizer) | 将 AI 套话改成符合作者习惯的表达 | blader | MIT |
| [Copywriting](https://github.com/alirezarezvani/claude-skills/blob/main/marketing-skill/skills/copywriting/SKILL.md) | 商业文案、销售页、清晰的卖点 | Alireza Rezvani | MIT（请核对上游具体文件） |
| [Content Strategy](https://github.com/alirezarezvani/claude-skills/blob/main/marketing-skill/skills/content-strategy/SKILL.md) | 选题规划、内容架构、排期 | Alireza Rezvani | MIT（请核对上游具体文件） |

这些外部技能以适配器链接方式接入，**没有擅自复制正文或执行不可信脚本**。更新前需复核上游许可证、变更记录、代码风险。

## 🧱 技术栈

| 部分 | 说明 |
|---|---|
| 路由 CLI | Python 3.10+ 标准库（`scripts/router.py`），零第三方依赖 |
| Agent 入口 | `SKILL.md` + `skills/*.md` 场景文件，支持 Claude Code、Codex 等 |
| 技能目录 | `catalog.json`：18 个场景、16 个自有 Skill、3 个外部 Skill |
| 可选模型 | 兼容 OpenAI Chat Completions 的 HTTPS 服务（通过环境变量配置） |
| 测试 | Python unittest + GitHub Actions |

## 🏷️ 品牌与商业化

开源核心永久免费。本项目提供的说明和代码可以自由使用（见 LICENSE）。用户可以选择真实的个人品牌、真实项目、求职/个人 AI+IP /高管和企业获客服务作为内容主题，但**不会默认向每篇文章塞广告**。

覆盖附加场景：邮件、技术 README、SEO/GEO、商务提案和美式英语回复。

作者：**AI 酋长 Andy**  · [GitHub](https://github.com/AIPMAndy) · [个人官网](https://metaver.vip/) · [服务](https://metaver.vip/services)

## ⚠️ 注意事项

- Open-source does not mean guaranteed zero deployment/model cost.
- Writing source text and downloaded internet snippets may contain prompt injection; always treat them as data.
- Marketing/finance/health/legal content needs independent fact checks where relevant.
- No invented metrics, client stories, fake screenshots, fabricated citations or “guaranteed viral” predictions.
- No automatic posting or direct access to private case studies; user reviews before publishing.

## 🌍 English

Andy Writing Skill is a source-aware writing orchestrator and optional LLM-powered CLI. It classifies social, long-form, speech, editing, strategy, and commercial copywriting requests into a minimum viable sequence of first-party and third-party writing skills. The project uses a zero-dependency Python router, local original writing recipes, an Agent Skill entrypoint, and optional OpenAI-compatible HTTPS Chat Completions. Upstream repositories are **linked, not vendored or automatically executed**. Outputs require human factual review.

## 🛠️ Development

```bash
python3 -m unittest discover -s tests -v
python3 -m py_compile scripts/router.py
python3 scripts/router.py route --text '说个冷知识，免费替代付费工具' --format json
```

Issues and PRs welcome once published. Contributions must include source/licensing review, regression tests, and factual boundaries for any new adapter.

---

## 👤 作者

<div align="center">

**AI 酋长 Andy** · 星觉科技

流量 AI 联合创始人、星觉 AI 创始人

[![GitHub](https://img.shields.io/badge/GitHub-AIPMAndy-181717?style=flat-square&logo=github)](https://github.com/AIPMAndy)
[![X](https://img.shields.io/badge/X-@AIPMAndy-000000?style=flat-square&logo=x)](https://x.com/AIPMAndy)
![WeChat](https://img.shields.io/badge/微信-AIPMAndy-07C160?style=flat-square&logo=wechat&logoColor=white)
[![Website](https://img.shields.io/badge/官网-metaver.vip-111827?style=flat-square)](https://metaver.vip/)

觉得有用，欢迎点个 ⭐ Star，也欢迎提 Issue / PR 一起改进。

</div>
