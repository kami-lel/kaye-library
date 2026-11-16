# kaye-library: Skill Catalog Documentation

[English](skill-catalog-doc.md) | 简体中文

kaye-library 全部 141 个技能一览。📚 分组与 [README](../README.zh-CN.md) 一致。

任何技能都有两种用法：

- 直接调用：输入技能名，例如 `/commit-sense`
- 直接说需求：说出你想做的事，例如“commit this”，智能体会自己挑选合适的技能

初来乍到？先试 🌟 首选，再看 ⭐ 推荐。

跳转到分组：[💻 编程](#-编程)、[📝 仓库与项目](#-仓库与项目)、[🎨 风格](#-风格)、[🗓️ 秘书](#️-秘书)、[🎮 Unity 引擎](#-unity-引擎)、[🖋️ 文书](#️-文书)、[🧱 基础元素](#-基础元素)、[🐙 Git](#-git)、[🤖 智能体](#-智能体)、[🪄 元提示词](#-元提示词)、[📖 术语表](#-术语表)。


































## 💻 编程

每种语言都写出整洁、一致的代码。不必再替 AI 收拾残局。

一切从 `/coder` 开始：所有代码共用的规范。每行不超过 80 个字符。命名始终一致。注释说明为什么，而不是怎么做。测试只跑改动涉及的部分，不必每次跑完整个测试套件。

你很少需要亲自调用 `/coder`。每个语言配置都会先调用它，再叠加自己的规则。Python 与 C# 共享同一套习惯，读起来却都像出自母语者之手。

整个会话都在写代码？`chat-coder` 把 `/chat` 的对话规则与 `/coder` 打包在一起。智能体会自行加载它，它不出现在斜杠菜单中。













### 语言配置

选择你的语言。多数配置会在智能体打开对应文件时自动加载。

| 技能 | 语言 | 你将得到 |
|---|---|---|
| `/coder-python` ⭐ | Python | PEP 8、一致的命名、Sphinx 文档字符串、阐明意图的注释 |
| `/coder-c` | C | C99 与整齐的大括号风格 |
| `/coder-cpp` | C++ | 统一的代码风格，基于 C 配置 |
| `/coder-ue` | Unreal Engine C++ | Unreal 的约定，基于 C++ 配置 |
| `/coder-c-sharp` | C# | 整齐的大括号与 XML 文档注释 |
| `/coder-javascript-and-typescript` | JavaScript、TypeScript | ES11、camelCase 命名、JSDoc 注释 |
| `/coder-html` | HTML | HTML5 结构与语义化标记 |
| `/coder-gdscript` | GDScript | 地道的 Godot 4 代码 |
| `/coder-powershell` | PowerShell | 统一固定的代码风格 |
| `/coder-bash-script` | Bash | 面向 Debian 的脚本、函数与库 |
| `/coder-bash-shell` | Bash | 只给出可直接粘贴的命令行 |

Python 另有两个附加技能。`/coder-python-docstring-style` 默认为每个函数、类与模块添加 Sphinx 文档字符串。`/coder-python-testing-guidelines` 编写符合项目约定的 `pytest` 测试。













### 保持代码健康

重构后测试全红？`/sync-unit-test` ⭐ 校正过时的断言、测试夹具与快照。如果真正出错的是代码，它会直说。真正的 bug 绝不会被掩盖。

快要发布了？`/review-gaps` ⭐ 先审查整个仓库。它赶在用户之前找出疏漏、偏差与半途而废的地方，并逐一标记，等你修复。













### 输出辅助

三个小技能，处理代码打印出的文字：

- `/coder-command-usage-message`：为 `--help` 与报错撰写简洁的用法说明
- `/coder-comment-banner-in-code-comment`：分级的横幅注释，标出文件标题、章节与小节
- `/coder-comment-banner-in-print-out`：分级的输出横幅，把日志、演示与测试运行分成清晰的阶段


































## 📝 仓库与项目

每个项目文件，都写得对、跟得上。

一个好项目面向五类读者。README 迎接访客。CHANGELOG 告诉用户改了什么。`AGENTS.md` 为 AI 智能体立规矩。`CONTEXT.md` 讲清架构。`docs/` 深入细节。kaye-library 为每一种都准备了撰写技能。

多数撰写技能都配有两个工作流。创建：从零写出文件。维护：代码变化后原地更新。

| 文件 | 读者 | 撰写 | 创建 | 维护 |
|---|---|---|---|---|
| `README.md` | 访客 | `/repo-readme-writer` 🌟 | `/create-readme` | `/maintain-readme` |
| `CHANGELOG.md` | 升级的用户 | `/repo-changelog-writer` | `/create-changelog` | `/maintain-changelog` |
| 仓库中的 `AGENTS.md` | AI 编程智能体 | `/repo-agents-writer` | `/create-repo-agents` | `/maintain-repo-agents` |
| 任意项目中的 `AGENTS.md` | AI 智能体 | `/proj-agents-writer` | `/create-project-agents` | `/maintain-project-agents` |
| `CONTEXT.md` | 新开发者与 AI | `/repo-context-writer` | ➖ | ➖ |
| 仓库中的 `docs/` | 想深入了解的读者 | `/repo-doc-writer` | `/create-repo-docs` | `/maintain-repo-docs` |
| 任意项目中的 `docs/` | 想深入了解的读者 | `/proj-doc-writer` | `/create-project-docs` | `/maintain-project-docs` |

`repo-` 技能面向代码仓库。`proj-` 技能适用于任何项目：游戏设计、研究资料，或代码库。

几个亮点：

- `/repo-readme-writer` 让空荡荡的仓库变成有人愿意读的首页，本库自己的 README 就是这样写成的
- `/repo-changelog-writer` 遵循 Keep a Changelog，附 `[Unreleased]` 区块与版本链接；`/create-changelog` 甚至能从 git 历史重建一份
- `/repo-agents-writer` 与 `/repo-context-writer` 把规则与知识分开：`AGENTS.md` 说该做什么，`CONTEXT.md` 说系统如何运作，个人笔记则放进私有的 `.local.md` 文件













### 初始化与日常整理

新仓库？`/initialize-repo` 一次写出整套起步文档：README、CHANGELOG、AGENTS、CONTEXT 与 `docs/`。不重复，不遗漏。只需要智能体规则？`/equip-proj-for-agent` 撰写并维护 `AGENTS.md`。两者都遵循 `/repo-structure`：每个文件夹与顶层文件的统一布局。

文件会膨胀。两个技能负责瘦身：

- `/condense-agents-and-context`：从 `AGENTS.md` 与 `CONTEXT.md` 中删去已完成的计划与过时细节，不添一字
- `/condense-changelog`：发布前精简 `[Unreleased]`，并标出破坏性变更

会话很长？`/maintenance-before-compact` 在上下文窗口压缩前，把每项持久变更存入 CHANGELOG、AGENTS 与 CONTEXT。学到的东西一点不丢。













### 合入功能与发布版本

两个工作流，各分两半：

| 准备 | 准备并收尾 | 收尾时多做的事 |
|---|---|---|
| `/ready-land-feature` | `/land-feature` | 以清晰的信息合并到 `dev` |
| `/ready-release-version` | `/release-version` ⭐ | 合并到 `main` 并打标签 |

准备的一半把改动记入 CHANGELOG，并同步所有文档。发布时，它还会为版本标注日期，并在每个元数据文件中升级版本号。想亲手合并？单独运行准备的一半即可。想改开 PR？请看 [Git](#-git) 中的 `/submit-pr`。













### 版本号

- `proj-version`：语义化版本规则，即 MAJOR、MINOR、PATCH 何时递增；自动加载，不出现在斜杠菜单中
- `/proj-version-extended`：`alpha`、`beta`、`rc` 编号，构建标签，以及每个开发阶段对应的版本
- `/proj-version-title`：根据新旧版本号撰写发布标题


































## 🎨 风格

无论智能体写什么，都是同一种声音。













### Markdown

- `style-markdown`：整洁的 GitHub Flavored Markdown，粗体与斜体用法一致；自动应用，不出现在斜杠菜单中
- `/style-markdown-extended`：带标签的列表、LaTeX 数学公式、Mermaid 图表
- `/style-markdown-footnotes`：每个脚注紧挨着引用它的文字
- `/style-markdown-endnotes`：所有定义集中在文末一处

长文档需要留白。`/style-heading-separation` 按标题级别与文件长度设置间距。`/style-heading-separation-medium` 与 `/style-heading-separation-long` 分别为中等与长篇文件固定间距。













### 大小写格式

每种约定各占一个技能，任何规则都能精确指向其中之一。

| 技能 | 约定 | 示例 |
|---|---|---|
| `/style-letter-case-title-case` | 主要单词首字母大写，次要单词小写 | `The Lord of the Rings` |
| `/style-letter-case-commentary-case` | 首字母小写，句末不加句号 | `check the Config first` |
| `/style-letter-case-snake-case` | 小写单词以下划线连接 | `total_price` |
| `/style-letter-case-kebab-case` | 小写单词以连字符连接 | `total-price` |
| `/style-letter-case-camel-case` | 首个单词小写，其后单词首字母大写 | `totalPrice` |
| `/style-letter-case-pascal-case` | 每个单词首字母大写，无分隔符 | `TotalPrice` |
| `/style-letter-case-all-caps` | 大写单词以下划线连接 | `TOTAL_PRICE` |













### 文风

两个技能，方向相反。`/style-briefness-style` ⭐ 把冗长的草稿压缩成紧凑的标题式笔记。最适合状态行、摘要与注释。`/style-good-writing` 以最轻的改动校对：拼写、语法、标点、清晰度。你的声音始终是你的。


































## 🗓️ 秘书

你的私人助理，打理收件箱、日历、待办清单与求职。它通过智能体已连接的应用工作。













### 每日与每周汇报

`/good-morning` 🌟 是你的每日简报。一条命令清理收件箱、回顾昨天、扫描今天的活动、寻找职位机会。你得到一份合并的报告。每一步也都能单独使用。

`/good-week` 展望本周的活动与职位机会。需要打打气？`/recap-yesterday` 与 `/recap-today` 用一句温暖、积极的话总结你完成的事。













### 邮件、日历与任务

`/draft-email` ⭐ 只写你要求的内容。绝不编造。随时按你的意见修改。`/sweep-email-inbox` 读取每封未读邮件，标为已读，并按类别归档。

日历与任务按推送与拉取成对出现：

| 推送到你的应用 | 拉取到对话中 |
|---|---|
| `/push-event-to-calendar`：一个活动，或对话中整理好的整份清单 | `/pull-event-from-calendar`：你真实的日程 |
| `/push-task-to-gtd`：附项目与艾森豪威尔象限的任务 | `/pull-task-from-gtd`：你真实的待办清单 |

GTD 即 *Getting Things Done*，一种任务管理方法。













### 活动与职位

`/scan-event-radar-daily` 查找今天的活动。`/scan-event-radar-weekly` 覆盖未来一周。两者都使用 `/secretary-event-brief-format`：标题、关键信息、简短概述。`/hunt-job-opportunity` 从任何来源汇集职位机会，每个职位一份简报。


































## 🎮 Unity 引擎

一套完整的 Unity 6 C# 代码规范。`/u3d` 奠定基础，并基于 `/coder-c-sharp`。每个主题各成一个技能，智能体只加载任务所需的部分。

| 技能 | 你将得到 |
|---|---|
| `/u3d-coding` | 统一习惯写法的 Unity C#；调试过程读起来像一个故事 |
| `/u3d-naming` ⭐ | 每个类、资源、文件夹与 GameObject 都遵循同一套命名规则；告别 `Hero_final2` |
| `/u3d-common-type-and-suffix` | 每个类、脚本、GameObject 与资源都有清晰的职责，由后缀命名 |
| `/u3d-if` | 设计师可以调整、重命名而不丢失已保存值的 Inspector 字段 |
| `/u3d-mb` | 每个 `MonoBehaviour` 都用同一种布局；缺失的 Inspector 引用在启动时就被发现 |
| `/u3d-so` | 每个 `ScriptableObject` 都用同一种布局；数据保持只读且有效 |
| `/u3d-pfb` | 尽早做成预制体与变体；改一处，处处更新 |
| `/u3d-game-tuning` | 游戏数值移入设计师可编辑的数据；调平衡无需重新编译 |
| `/u3d-owner-driven-activation` | 由一个所有者生成、显示与隐藏每个短暂存在的对象；闲置时零开销 |
| `/u3d-assets-management` | `Assets/` 下每个资源都有固定位置；无需搜索即可找到 |


































## 🖋️ 文书

你的学术书记员：引注、笔记、会议纪要与细致的修订。













### 引注

所有引注都遵循 *Chicago Manual of Style*。再也不用手动排版。

- `/amanuensis-chicago-note` ⭐：以原生 Markdown 脚注呈现的引注
- `/amanuensis-chicago-bibliography`：参考文献条目，普通或附注释
- `/assemble-bibliography`：把文档引用的所有来源汇集成一份参考文献
- `/bibliographer`：当一篇文章既需要脚注又需要参考文献时，统筹以上所有技能













### 笔记与记录

`/dispositor` 是基础的笔记员：结构化笔记，统一的文件名，统一的布局。四位专家基于它工作：

- `/scholiast`：逐段的学术阅读笔记，可按需附上引注
- `/minutes-clerk`：追踪每项决定与待办事项直至完成的会议纪要
- `/config-writer`：把应用、游戏或系统的设置保存为可恢复的快照
- `/keybinding-writer`：以紧凑的按键符号记录快捷键

还有 `/redactor`：修订你的文字，保留你的意图与风格，反复打磨直到通顺。


































## 🧱 基础元素

支撑其他所有技能的小而精确的构件。其他技能会替你调用它们。只想要某一条规则时，也可以直接调用。

日期与时间处处一致：

| 技能 | 作用 |
|---|---|
| `/element-dt-year-month-day-format` | 含年份的日期，星期可选 |
| `/element-dt-month-day-format` | 不含年份的日期，星期可选 |
| `/element-dt-time-format` | 24 小时制时间，精度从分钟到小数秒 |
| `/element-dt-watch-day` | 按 30 小时制延续过午夜的一天，专为夜猫子设计 |
| `/element-dt-watch-week` | 总在周日结束的规划周 |

更多构件：

- `/element-numerical-values-with-units`：公制与美制单位并列，缩写准确
- `/element-international-phonetic-alphabet`：在任何难读的词后附上国际音标，适用于所有语言
- `/element-alphabetical-sequence-numbering`：用圆圈字母（ⓐ、ⓑ、ⓒ）标注选项，回答只需一个字母
- `/element-triage-tags`：`BUG`、`FIXME`、`TODO` 与 `HACK`，分三档响亮程度
- `/sort-and-group-triage-tag`：把现有标签整理成清晰的分组，其他一概不动


































## 🐙 Git

值得一读的提交。干净的合并。并行工作互不冲突。

`/working-with-git` 立下基本规则：未经你同意，智能体绝不推送，也绝不改写历史。在用 Perforce？`/working-with-p4v` 为每个 Perforce 术语配上对应的 Git 术语。不必在脑中翻译。













### 提交与合并

`/commit-sense` 🌟 告别“fix stuff”式的提交。说一句“commit this”，即可得到精准的摘要行，以及逐文件说明改了什么、为什么改的清单。`/commit-sense-branch-merging` 为合并信息做同样的事。

分支生命周期的其余环节：

- `/resolve-merge-conflict` ⭐：解开卡住的合并，调和双方改动，清除冲突标记
- `/prune-merged-branches`：删除已合并的分支，并报告删了什么、留了什么
- `/submit-pr`：准备好文档并向 `dev` 提交 PR，标题与正文替你写好













### 在工作树中并行工作

同时推进三个功能。互不冲突。关联工作树是另一个工作文件夹，位于自己的分支上。`/tend-linked-wt` ⭐ 管理它的整个生命周期：`/plant-linked-wt` 创建它，`/uproot-linked-wt` 在工作合并后移除它。


































## 🤖 智能体

智能体如何与你协作，一轮又一轮。`/chat` 设定对话规则：回复语言、每个步骤的共享术语，以及醒目标记、不会错过的提问。













### Movement 与 Suite

大任务需要结构。Suite 是整个多轮任务。Movement 是其中可审阅的一步，小到一眼就能判断。`/agent-movement-and-suite` 定义两者。`/agent-movement-and-suite-with-count` 把 Movement 再拆成 Count，进度以分数呈现。

`/plan-for-suite` 🌟 把它付诸实践。不再一口气改动 30 个文件。智能体先勘察仓库，写出编号的计划，再等待你的批准。

- `/execute-plan-for-suite`：每轮执行一个 Movement；计划文件保存进度，今晚暂停，明天继续，换个会话也行
- `/rework-plan-for-suite`：计划与现实不符？它会暂停、重写计划，并再次等待你的批准

节奏由你决定。`/halt-each-movement` 每一步后停下，等你审阅。`/cascade-all-movements` 一口气跑完剩余步骤，只在完成或需要你时停下。


































## 🪄 元提示词

写提示词的提示词。`/write-llm-prompt` ⭐ 把含糊的系统提示词变成真正好用的提示词：起草、评估、打磨，JSON schema 与原有结构保持不变。

另外三个撰写告诉智能体何时加载技能的元数据：

- `/write-skill-description`：技能做什么，主要动词打头
- `/write-skill-when-to-use`：触发短语，以及技能的边界
- `/write-skill-description-and-when-to-use`：两者一起写


































## 📖 术语表

少打几个字。智能体照样听懂。每份术语表解码一类缩写。

| 技能 | 解码 | 示例 |
|---|---|---|
| `/glossary-coder-abbr` | 编程缩写 | `ctor`、`iface`、`mpl` |
| `/glossary-programming-language-codes` | 编程语言代码 | `py`、`ts`、`cpp` |
| `/glossary-natural-language-codes` | 自然语言代码 | `en`、`zh`、`jp` |
| `/glossary-units-of-measure` | 计量单位缩写 | `ft`、`lb`、`mi` |
| `/glossary-element-dt-days-of-week` | 单字母星期代码 | 用于日期与日程 |
| `/glossary-secretary-eisenhower-matrix-quadrant` | 艾森豪威尔矩阵四象限 | 按重要与紧急划分，附表情符号 |
