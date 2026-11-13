# kaye-library README

[English](README.md) | 简体中文

> 本文为 [README.md](README.md) 的简体中文译本，可能滞后于英文版；如有出入，以英文版为准。

📚 **100+ 个开箱即用的 Agent Skills**，让你的 AI 助手像一位严谨的专业人士那样写作、编程、提交、规划与整理。一次安装，每一次对话都更出色。✨

⭐ **如果 kaye-library 帮你省下了一两条提示词，欢迎 [在 GitHub 上点个 Star](https://github.com/kami-lel/kaye-library)！** 每一颗星都能让更多人发现它。🙏

## 💡 为什么选择 kaye-library？

每次向 AI 解释你的提交风格、Markdown 偏好，或 README 应该长什么样时，你都在重写一条别人早已打磨好的提示词。kaye-library 把这些提示词汇集成一个精选库，并以技能（skill）的形式交给你的智能体，由它自行调用。

- 🧠 一次编写，永久复用：每条指令只存放在一处，随你的智能体到达任何地方
- 🎯 自动触发：说一句“commit this”或“write a README”，对应的技能就会接手
- 🧩 易于扩展：在其上叠加你自己的包，覆盖任意技能，保留其余部分，详见 [Consumer 文档](https://github.com/kami-lel/kaye-engine/blob/dev/docs/consumer-doc.md)
- 📦 随处可用：Agent Skills 文件夹、Claude 插件、插件市场，或可直接上传的 `.zip`

## 🗂️ 包含内容

100+ 个技能，分为 11 组：

| | 分组 | 你的智能体将学会 |
|---|---|---|
| 💻 | 编程 | 通用编码规则、规划与审查工作流、测试同步，以及 Bash、C、C++、C#、GDScript、HTML、JS/TS、PowerShell、Python、Unreal Engine 的语言配置 |
| 📝 | 仓库与项目 | README、CHANGELOG、AGENTS、CONTEXT 及文档的撰写；功能合入与版本发布工作流 |
| 🎨 | 风格 | Markdown、标题间距、各种大小写格式、精简文风、优质写作 |
| 🗓️ | 秘书 | 邮件起草与清理、日历与任务同步、活动雷达、每日回顾、早间与每周汇报、求职 |
| 🎮 | Unity 引擎 | Unity 6 C# 命名、Inspector 字段、输入、激活、游戏调参、资源放置 |
| 🖋️ | 文书 | 芝加哥格式引注与参考文献、信息脱敏、笔记、配置文件、快捷键、会议纪要 |
| 🧱 | 基础元素 | 日期与时间格式、计量单位、分诊标签、国际音标 |
| 🐙 | Git | 附逐文件清单的提交信息、合并冲突解决、分支清理、PR、Git 与 Perforce 术语 |
| 🤖 | 智能体 | 对话规则、Movement 与 Suite 规划：将大任务拆分为可审阅的步骤 |
| 🪄 | 元提示词 | LLM 系统提示词与技能描述的撰写 |
| 📖 | 术语表 | 计量单位、星期、语言代码、编程缩写 |

推荐先试试这几个：

- `/commit-sense`：🐙 说一句“commit this”，即可得到清晰的摘要行，以及逐文件说明改了什么、为什么改的清单
- `/repo-readme-writer`：📝 把一个空荡荡的仓库变成易于浏览的首页，涵盖用途、安装与用法，就像本页这样
- `/coder-python`：💻 整洁、符合 PEP 8 的 Python 代码，命名一致，附 Sphinx 文档字符串和阐明意图的注释
- `/plan-for-suite`：🤖 把庞杂的任务拆分为编号的、可审阅的步骤，每一步开始前都等待你的批准
- `/good-morning`：🗓️ 一份早间报告：清理收件箱、回顾昨天，并呈现即将到来的活动与职位机会

## 🚀 快速开始

### 在 Claude 中使用

**Claude Desktop**：[GitHub Releases 页面](https://github.com/kami-lel/kaye-library/releases) 上的每个版本都附带现成的插件 `.zip`，文件名为 `kaye-library-claude-VERSION.zip`。下载后按照 [Use in Claude Desktop](https://github.com/kami-lel/kaye-engine/blob/dev/docs/claude-doc.md#use-in-claude-desktop) 在应用中上传即可，无需安装。

**Claude Code VS Code 扩展**：按照 [Use in the Claude Code VS Code Extension](https://github.com/kami-lel/kaye-engine/blob/dev/docs/claude-doc.md#use-in-the-claude-code-vs-code-extension) 操作，将其中的 `kaye-engine` 替换为 `kaye-library`。

### 📦 使用 pip 安装

需要 Python 3.11 或更高版本。🐍

```bash
pip install git+https://github.com/kami-lel/kaye-library.git
kaye-library skill --all ./skills   # export every skill into ./skills
```

## 🧭 探索

```bash
kaye-library x ls                            # every skill
kaye-library blueprint render commit-sense   # preview one prompt
kaye-library --help                          # everything else
```

各技能之间如何依赖与相互调用，请参阅 [blueprint 文档](docs/blueprint-doc.md)。

## 🤝 参与贡献

欢迎提交新技能与修复！🛠️ 先安装一份可编辑的工作副本，再运行你所改动部分的测试：

```bash
pip install -e '.[dev]'
pytest tests/skill_export_test.py
```

入门路径，按顺序：

1. 找到技能所在位置：每个功能分组在 `kaye_library/registrations/` 下都有一个文件夹，其 Markdown 语料与注册它的代码放在一起；[blueprint 文档](docs/blueprint-doc.md) 展示了各技能之间的关联
2. 了解底层引擎：技能所用的 Markdown 格式见 [corpus 文档](https://github.com/kami-lel/kaye-engine/blob/dev/docs/corpus-doc.md)，其 `{description}` 与 `{when_to_use}` 附注见 [sidecar 文档](https://github.com/kami-lel/kaye-engine/blob/dev/docs/sidecar-doc.md)，blueprint 与注册表见 [prompt 文档](https://github.com/kami-lel/kaye-engine/blob/dev/docs/prompt-doc.md)，导出选项见 [exportable registry 文档](https://github.com/kami-lel/kaye-engine/blob/dev/docs/exportable-registry-doc.md)，术语表见 [abbreviation 文档](https://github.com/kami-lel/kaye-engine/blob/dev/docs/abbrs-doc.md)
3. 在库之上构建，而非修改它：[Consumer 文档](https://github.com/kami-lel/kaye-engine/blob/dev/docs/consumer-doc.md) 介绍如何叠加你自己的包并覆盖某个技能，[examples/minimal-consumer](examples/minimal-consumer/example_consumer/__init__.py) 中有一个可运行的示例包

请牢记一条规则：这里的每条提示词都不含个人数据。

## 🙌 致谢

基于 [kaye-engine](https://github.com/kami-lel/kaye-engine) 构建，它负责解析 Markdown 语料并渲染每一条提示词。⚙️

⭐ 喜欢吗？在 GitHub 上 [点个 Star](https://github.com/kami-lel/kaye-library) 就是莫大的支持！
