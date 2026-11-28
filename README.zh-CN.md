# kaye-library README

[English](README.md) | 简体中文

📚 **140+** 个开箱即用的 **Agent Skills**，让 AI 助手像资深从业者一样写文档、写代码、提交代码、做规划、整理资料。🪶 更省 **token**、🔁 结果**稳定可复现**、⚡ 多个智能体**并行**开工：装一次，以后每次对话都更靠谱。✨

⚙️ 底层由 **[kaye-engine](https://github.com/kami-lel/kaye-engine)** 驱动。它是本项目的姊妹仓库，负责渲染和导出所有技能。

⭐ 如果 kaye-library 帮你省了几条提示词，欢迎 **[到 GitHub 点个 Star](https://github.com/kami-lel/kaye-library)**！每一颗星都能让更多人看到它。🙏

## 💡 为什么选择 kaye-library？

你的提交风格、Markdown 习惯、README 该怎么写……每跟 AI 解释一遍，就是把别人早已打磨好的提示词重写一遍，还白白烧掉 **token**。kaye-library 把这些提示词整理成一个精选库，拆成一个个小而精的技能[skill]，让智能体按需取用。

- 🪶 **省 Token**：一条臃肿的系统提示词，拆成 140+ 个各管一摊的**小技能**；智能体**只加载**手头任务用得上的那个，**上下文窗口**[context window]留给你的代码。精简文风还能让注释、笔记和提交信息写得更短，输出的 token 也更省
- 🔁 **稳定可复现**：同样的需求，每次都按**同样的方式**处理。从提交信息到发布清单，你认可过一次的流程，跑到第一百次照样靠谱；大任务的进度保存在**计划文件**[plan file]里，今晚停下，明天接着干
- ⚡ **天生支持并行**：每个子智能体[subagent]、每个工作树都加载同一套技能，五个智能体照着**同一本规矩**干活；`/tend-linked-wt` 还给每个任务单独开一个**工作树**，并行的分支互不打架
- 🔗 **技能联动**：技能之间可以互相调用。`/good-morning` 一口气跑完四份报告，`/release-version` 从更新文档、升版本号到合并、打标签一条龙；通用规则**只写一次**，几十个技能共用，改一处，处处生效
- 🎯 **自动触发**：说一句“提交一下”或“写个 README”，对应的技能就会自己上场
- 🧩 **方便扩展**：在它之上叠加你自己的包，想覆盖哪个技能就覆盖哪个，其余照常可用，详见 [Consumer 文档](https://github.com/kami-lel/kaye-engine/blob/dev/docs/consumer-doc.md)
- 🔒 **隐私优先**：所有提示词都不含**个人数据**，每次改动都会跑隐私测试，扫描全部发布文件
- 📦 **多端通用**：Claude Code、Claude Desktop、Codex 插件，插件市场，Agent Skills 文件夹，可直接上传的 `.zip`，连 Continue 规则、Hermes 和 Open WebUI 也支持

## 🗂️ 包含内容

140+ 个技能，共 11 组：

| | 分组 | 智能体能学到什么 |
|---|---|---|
| 🤖 | 智能体 | 对话规则，Movement、Voice 与 Suite 规划：把大任务拆成一步步可审阅的小块，纯智能体 Voice 并行推进 |
| 📝 | 仓库与项目 | README、CHANGELOG、AGENTS、CONTEXT 和 docs 的撰写；功能合入与版本发布流程 |
| 🐙 | Git | 带逐文件清单的提交信息、合并冲突处理、清理分支、给并行任务用的关联工作树、PR、Git 与 Perforce 术语对照 |
| 💻 | 编程 | 通用编码规范、规划与代码审查流程、测试同步，外加 Bash、C、C++、C#、GDScript、HTML、JS/TS、PowerShell、Python、Unreal Engine 的语言规范 |
| 🗓️ | 秘书 | 写邮件、清理收件箱、同步日历和待办、活动雷达、每日回顾、早报和周报、找工作 |
| 🖋️ | 文书 | 芝加哥格式脚注和参考文献、文字修订、笔记、配置记录、快捷键记录、会议纪要 |
| 🎮 | Unity 引擎 | Unity 6 C# 命名、Inspector 字段、输入、对象激活、数值调优、资源摆放 |
| 🪄 | 元提示词 | 写 LLM 系统提示词和技能描述 |
| 🎨 | 风格 | Markdown、标题间距、各类大小写命名、精简文风、文字润色 |
| 🧱 | 基础元素 | 日期时间格式、计量单位、TODO 类标签、国际音标 |
| 📖 | 术语表 | 计量单位、星期、语言代码、编程缩写 |

#### 🌟 先从这些首选开始

- `/commit-sense`：🐙 跟“fix stuff”式提交说再见：说一句“提交一下”，就能得到一行精准的**摘要**，外加逐文件的**改动清单**，写清改了什么、为什么改
- `/plan-for-suite`：🤖 别再让智能体一口气改 30 个文件：大活拆成编号的**小步骤**，每一步都等你点头再动手
- `/tend-linked-wt`：🐙 三个功能同时开发也互不干扰：每个任务一个独立的**关联工作树**，合入后随即清理
- `/initialize-repo`：📝 新建仓库时，一次配齐整套**起步文档**：README、CHANGELOG、AGENTS、CONTEXT 和 docs，不重不漏
- `/sync-unit-test`：💻 一重构，测试就全挂？自动修正**过时的断言**和 fixture，真正该改代码的地方也会替你标出来
- `/good-morning`：🗓️ 早上不用在一堆标签页之间来回切：**一份报告**搞定收件箱、回顾昨天，再把近期活动和招聘机会一并列出
- `/amanuensis-chicago-note`：🖋️ 引注再也不用手动排版：按芝加哥格式自动生成**原生 Markdown 脚注**

#### ⭐ 再看看这些推荐

- `/coder-python`：💻 不用再手动收拾 AI 写的代码：符合 PEP 8，命名统一，附 Sphinx 风格的 docstring，注释讲清意图
- `/review-gaps`：💻 发布前把整个仓库过一遍，赶在用户之前揪出没收尾的地方
- `/release-version`：📝 发版不用再对着清单提心吊胆：文档和变更日志更新到位、版本号升好、合并到 `main` 并打上标签
- `/repo-readme-writer`：📝 把空荡荡的仓库变成让人愿意读下去的首页，用途、安装、用法一应俱全，本页就是这么写出来的
- `/maintenance-before-compact`：📝 会话太长，上下文快要压缩了？先把所有长期有效的改动记进 CHANGELOG、AGENTS 和 CONTEXT，积累的信息一点不丢
- `/style-briefness-style`：🎨 把啰嗦的草稿压缩成新闻标题式的精简笔记
- `/draft-email`：🗓️ 邮件只写你交代的内容，绝不自作主张，想改几遍改几遍
- `/u3d-naming`：🎮 终结 `Hero_final2` 式的命名混乱：Unity 里的类、资源、文件夹和 GameObject 全按同一套规则命名
- `/minutes-clerk`：🖋️ 会议纪要记下每项决议和待办，一路跟进到落实为止
- `/element-dt-watch-day`：🧱 按 30 小时制计算的“一天”：过了午夜还算今天，夜猫子专用
- `/resolve-merge-conflict`：🐙 合并卡住了？帮你理清冲突：每个冲突块都兼顾双方的改动，并把冲突标记清理干净
- `/write-llm-prompt`：🪄 把含糊的系统提示词改成真正好用的版本：起草、打分、打磨一条龙

📚 想按名称查看全部技能？**[技能目录](docs/skill-catalog-doc.zh-CN.md)** 是**全部技能**的完整清单，逐一说明用途与调用方式。

## 🚀 快速开始

### 在 Anthropic Claude 中使用

在用 Claude Desktop 或 VS Code 扩展？[看分步安装指南](docs/claude-usage-doc.zh-CN.md)，Windows 和 Linux 还有一键安装包。

### 在 OpenAI Codex 中使用

在用 Codex？[看看怎么安装 kaye-library](docs/codex-usage-doc.zh-CN.md)。

### 📦 用 pip 安装

需要 Python 3.11 及以上版本。🐍

```bash
pip install git+https://github.com/kami-lel/kaye-library.git
kaye-library skill --all ./skills   # 把全部技能导出到 ./skills
```

## 🧭 探索

```bash
kaye-library x ls                            # 列出全部技能
kaye-library blueprint render commit-sense   # 预览单个提示词
kaye-library --help                          # 查看其余命令
```

技能之间怎么依赖、怎么互相调用，见 [blueprint 文档](docs/blueprint-doc.md)。

## 🤝 参与贡献

欢迎贡献新技能和修复！🛠️ 先以可编辑模式[editable]安装本地仓库，再只针对你改动的部分跑测试：

```bash
pip install -e '.[dev]'
pytest tests/skill_export_test.py
```

上手路线，按顺序来：

1. 找到技能放在哪：每个功能分组在 `kaye_library/registrations/` 下都有自己的目录，Markdown 语料和注册代码放在一起；[blueprint 文档](docs/blueprint-doc.md) 画出了技能之间的关系
2. 了解底层引擎：技能用的 Markdown 格式见 [corpus 文档](https://github.com/kami-lel/kaye-engine/blob/dev/docs/corpus-doc.md)，`{description}` 和 `{when_to_use}` 附注见 [sidecar 文档](https://github.com/kami-lel/kaye-engine/blob/dev/docs/sidecar-doc.md)，blueprint 和注册表见 [prompt 文档](https://github.com/kami-lel/kaye-engine/blob/dev/docs/prompt-doc.md)，导出选项见 [exportable registry 文档](https://github.com/kami-lel/kaye-engine/blob/dev/docs/exportable-registry-doc.md)，术语表见 [abbreviation 文档](https://github.com/kami-lel/kaye-engine/blob/dev/docs/abbrs-doc.md)
3. 在库的基础上扩展，而不是直接改它：[Consumer 文档](https://github.com/kami-lel/kaye-engine/blob/dev/docs/consumer-doc.md) 讲了怎么叠加自己的包、覆盖某个技能，[examples/minimal-consumer](examples/minimal-consumer/example_consumer/__init__.py) 里有一个能直接跑的示例包

只有一条硬性规定：这里的提示词一律不含个人数据。完整的约定、命令和限制见 [AGENTS.md](AGENTS.md)，背后的架构见 [CONTEXT.md](CONTEXT.md)。

----

⭐ 觉得好用？到 GitHub [点个 Star](https://github.com/kami-lel/kaye-library) 就是最大的支持！
