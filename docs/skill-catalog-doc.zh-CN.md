# Kaye Library：技能目录

[English](skill-catalog-doc.md) | 简体中文

kaye-library 的 148 个技能，全在这里。📚 分组和 [README](../README.zh-CN.md) 保持一致。

用法有两种：

- 直接调用：输入技能名，比如 `/commit-sense`
- 直接开口：说出你要做的事，比如“commit this”，智能体会自己挑合适的技能

第一次来？先试试 🌟 首选，再看看 ⭐ 推荐。

快速跳转：[💻 编程](#-编程)、[📝 仓库与项目](#-仓库与项目)、[🎨 风格](#-风格)、[🗓️ 秘书](#️-秘书)、[🎮 Unity 引擎](#-unity-引擎)、[🖋️ 文书](#️-文书)、[🧱 基础元素](#-基础元素)、[🐙 Git](#-git)、[🤖 智能体](#-智能体)、[🪄 元提示词](#-元提示词)、[📖 术语表](#-术语表)。


































## 💻 编程

不管什么语言，代码都干净统一。再也不用替 AI 收拾烂摊子。

一切从 `/coder` 开始，它是所有代码共用的基本规范：每行不超过 80 个字符，命名前后一致，注释讲“为什么”而不是“怎么做”，测试只跑改动波及的部分，不用每次都跑全套。

`/coder` 一般不用你亲自调用。各语言规范都会先加载它，再叠加自己的规则。所以 Python 和 C# 守的是同一套习惯，写出来却都很地道。

一整场会话都在写代码？`chat-coder` 把 `/chat` 的对话规则和 `/coder` 打包在一起，由智能体自动加载，斜杠菜单里看不到它。













### 语言规范

挑你要写的语言就行。大多数规范还会在智能体打开对应文件时自动加载。

| 技能 | 语言 | 能带来什么 |
|---|---|---|
| `/coder-python` ⭐ | Python | 遵循 PEP 8，命名统一，附 Sphinx 文档字符串，注释讲清意图 |
| `/coder-c` | C | C99，大括号风格统一 |
| `/coder-cpp` | C++ | 统一的 C++ 风格，以 C 规范为基础 |
| `/coder-ue` | Unreal Engine C++ | Unreal 的编码约定，以 C++ 规范为基础 |
| `/coder-c-sharp` | C# | 统一的大括号风格，配 XML 文档注释 |
| `/coder-javascript-and-typescript` | JavaScript、TypeScript | 以 ES11 为准，camelCase 命名，JSDoc 注释 |
| `/coder-html` | HTML | 规范的 HTML5 结构和语义化标签 |
| `/coder-gdscript` | GDScript | 地道的 Godot 4 写法 |
| `/coder-powershell` | PowerShell | 一套固定的代码风格 |
| `/coder-bash-script` | Bash | 面向 Debian 的脚本、函数和函数库 |
| `/coder-bash-shell` | Bash | 只给一行命令，复制就能用 |

Python 还有两个搭档：`/coder-python-docstring-style` 默认给每个函数、类和模块配上 Sphinx 文档字符串；`/coder-python-testing-guidelines` 按项目自己的约定写 `pytest` 测试。













### 代码体检

一重构测试就全红？`/sync-unit-test` 🌟 帮你修正过时的断言、测试夹具和快照。要是真正出问题的是代码，它会直接告诉你，绝不把真 bug 糊弄过去。

快发版了？先用 `/review-gaps` ⭐ 把整个仓库过一遍。它会赶在用户之前，把遗漏、跑偏和没收尾的地方都找出来，逐个打上标记，等你处理。













### 输出小帮手

三个小技能，专管代码打印出来的文字：

- `/coder-command-usage-message`：给 `--help` 和报错信息写简洁的用法说明
- `/coder-comment-banner-in-code-comment`：在源码里用分级横幅注释标出文件标题、章节和小节
- `/coder-comment-banner-in-print-out`：在程序输出里用分级横幅，把日志、演示和测试过程分成清楚的阶段


































## 📝 仓库与项目

项目里的每份文件，都写得对、跟得上。

一个好项目要照顾五类读者：README 给访客看，CHANGELOG 告诉用户改了什么，`AGENTS.md` 给 AI 智能体立规矩，`CONTEXT.md` 讲清架构，`docs/` 负责深入细节。另有两份可选文件：`CREDITS.md` 为每项第三方素材署名，`DEVLOG.md` 记下团队的开发日志。kaye-library 给每一类都配了专门的写作技能。

大多数写作技能还配了两个工作流：“创建”从零写出文件，“维护”在代码更新后就地改好。

| 文件 | 写给谁 | 写作 | 创建 | 维护 |
|---|---|---|---|---|
| `README.md` | 访客 | `/repo-readme-writer` ⭐ | `/create-readme` | `/maintain-readme` |
| `CHANGELOG.md` | 要升级的用户 | `/repo-changelog-writer` | `/create-changelog` | `/maintain-changelog` |
| `AGENTS.md`（代码仓库） | AI 编程智能体 | `/repo-agents-writer` | `/create-repo-agents` | `/maintain-repo-agents` |
| `AGENTS.md`（任意项目） | AI 智能体 | `/proj-agents-writer` | `/create-project-agents` | `/maintain-project-agents` |
| `CONTEXT.md` | 新加入的开发者和 AI | `/repo-context-writer` | ➖ | ➖ |
| `CREDITS.md` | 被署名的创作者、核查授权的人 | `/repo-credits-writer` | `/create-credits` | `/maintain-credits` |
| `DEVLOG.md` | 团队、评审者 | `/repo-devlog-writer` | `/create-devlog` | `/maintain-devlog` |
| `docs/`（代码仓库） | 想深入了解的读者 | `/repo-doc-writer` | `/create-repo-docs` | `/maintain-repo-docs` |
| `docs/`（任意项目） | 想深入了解的读者 | `/proj-doc-writer` | `/create-project-docs` | `/maintain-project-docs` |

`repo-` 系列面向代码仓库，`proj-` 系列什么项目都能用：游戏策划、研究资料、代码库都行。

几个亮点：

- `/repo-readme-writer` 能把光秃秃的仓库变成有人愿意看的首页，本库的 README 就是这么来的
- `/repo-changelog-writer` 遵循 Keep a Changelog 规范，带 `[Unreleased]` 区块和版本链接；`/create-changelog` 甚至能从 git 历史里重建一份
- `/repo-credits-writer` 给每项第三方素材一行记录：路径、来源、作者、授权，不让任何素材无名上线
- `/repo-devlog-writer` 把每项改动和促成它的试玩、问卷或 bug 对上号，配带说明的截图，并如实记下遗留问题
- `/repo-agents-writer` 和 `/repo-context-writer` 让规则和知识各归各位：`AGENTS.md` 写该怎么做，`CONTEXT.md` 写系统怎么运作，个人笔记则放进只属于你自己的 `.local.md` 文件













### 起步与整理

新建仓库？`/initialize-repo` 🌟 一次写齐全套起步文档：README、CHANGELOG、AGENTS、CONTEXT 和 `docs/`，不重复，不遗漏。只想给智能体立规矩？`/equip-proj-for-agent` 负责写好并维护 `AGENTS.md`。两者都遵循 `/repo-structure`，所有文件夹和顶层文件都按同一套布局摆放。

文件用久了会越来越臃肿，这两个技能帮它瘦身：

- `/condense-agents-and-context`：删掉 `AGENTS.md` 和 `CONTEXT.md` 里已完成的计划和过时内容，只减不增
- `/condense-changelog`：发版前精简 `[Unreleased]`，顺便标出破坏性变更

会话拉得很长？`/maintenance-before-compact` ⭐ 会在上下文压缩之前，把所有长期有效的改动记进 CHANGELOG、AGENTS 和 CONTEXT，辛苦攒下的信息一点不丢。













### 合入功能，发布版本

两个工作流，合并前有准备的一半，合并后有清理的一半：

| 只做准备 | 只做清理 | 准备、合并加清理 | 合并多做什么 |
|---|---|---|---|
| `/ready-land-feature` | `/scrub-landed-feature` | `/land-feature` | 合并到 `dev`，附上清晰的合并信息 |
| `/ready-release-version` | `/scrub-released-version` | `/release-version` ⭐ | 合并到 `main`，打上版本标签 |

准备阶段会把改动记进 CHANGELOG，并同步所有相关文档；发版时还会给版本标上日期，并在所有元数据文件里升好版本号。清理阶段先推送结果，再收拾合并留下的东西：合入功能后是已合并的分支和它的关联工作树，发版后是已合并的分支和落后的 `dev`，随后把 `dev` 升到下一个 alpha 版本，每一步都等你批准才做。想自己手动合并？先跑准备那一半，合并，再跑清理那一半。想走 PR？见 [Git](#-git) 分组里的 `/submit-pr`。













### 版本号

- `proj-version`：语义化版本规则，也就是 MAJOR、MINOR、PATCH 什么时候该升；自动加载，斜杠菜单里看不到
- `/proj-version-extended`：`alpha`、`beta`、`rc` 预发布编号、构建标签，以及每个开发阶段该用什么版本号
- `/proj-version-title`：根据新旧版本号起发布标题


































## 🎨 风格

不管写什么，智能体都是同一种文风。













### Markdown

- `style-markdown`：规范的 GitHub Flavored Markdown，粗体、斜体用法统一；自动生效，斜杠菜单里看不到
- `/style-markdown-extended`：带标签的列表、LaTeX 公式、Mermaid 图表
- `/style-markdown-footnotes`：脚注就近放在引用它的文字旁边
- `/style-markdown-endnotes`：所有注释统一放到文末
- `/style-markdown-file-assets`：每个文件的图片放进它专属的同级文件夹，如 `CHANGELOG-assets/`，用相对路径链接

长文档要留白才好读。`/style-heading-separation` 按标题层级和文件长短安排空行；`/style-heading-separation-medium` 和 `/style-heading-separation-long` 则直接套用中篇和长篇的间距。













### 大小写格式

每种格式单独一个技能，其他规则引用时一指一个准。

| 技能 | 格式 | 示例 |
|---|---|---|
| `/style-letter-case-title-case` | 实词首字母大写，虚词小写 | `The Lord of the Rings` |
| `/style-letter-case-commentary-case` | 句首小写，句末不加句号 | `check the Config first` |
| `/style-letter-case-snake-case` | 小写单词用下划线连接 | `total_price` |
| `/style-letter-case-kebab-case` | 小写单词用连字符连接 | `total-price` |
| `/style-letter-case-camel-case` | 首个单词小写，后面每个单词首字母大写 | `totalPrice` |
| `/style-letter-case-pascal-case` | 每个单词首字母大写，不加分隔符 | `TotalPrice` |
| `/style-letter-case-all-caps` | 全大写，单词之间用下划线连接 | `TOTAL_PRICE` |













### 文风

两个技能，方向正好相反。`/style-briefness-style` ⭐ 把啰嗦的草稿压成干脆的标题式笔记，写状态、摘要、注释都合适。`/style-good-writing` 则只做最小改动的校对：拼写、语法、标点、表达是否清楚，原有的语气和用词都保留。


































## 🗓️ 秘书

收件箱、日历、待办、求职，一个私人助理全包了。它直接用智能体已经接入的那些应用干活。













### 早报与周报

`/good-morning` 🌟 是你的每日早报。一条命令清理收件箱、回顾昨天、扫一遍今天的活动、找找招聘机会，最后汇总成一份报告。每一步也都能单独用。

`/good-week` 帮你提前看看这周的活动和招聘机会。想给自己打打气？`/recap-yesterday` 和 `/recap-today` 会用一句暖心的话，总结你昨天或今天完成了什么。













### 邮件、日历和待办

`/draft-email` ⭐ 只写你交代的内容，不添油加醋，想改几遍改几遍。`/sweep-email-inbox` 把每封未读邮件看一遍、标成已读，再分门别类归好。

日历和待办都是“推”“拉”成对：

| 推到你的应用里 | 拉进对话里 |
|---|---|
| `/push-event-to-calendar`：加一个活动，或者把对话里整理好的一整串活动都加进去 | `/pull-event-from-calendar`：把你真实的日程拉进来 |
| `/push-task-to-gtd`：添加任务，每条都带上所属项目和艾森豪威尔象限 | `/pull-task-from-gtd`：把你真实的待办清单拉进来 |

GTD 是 *Getting Things Done* 的缩写，一种经典的任务管理方法。













### 活动和招聘

`/scan-event-radar-daily` 找今天的活动，`/scan-event-radar-weekly` 看未来一周。两者都按 `/secretary-event-brief-format` 的格式输出：标题、关键信息、一段简短概述。`/hunt-job-opportunity` 从各种渠道收集招聘信息，每个职位一份简报。


































## 🎮 Unity 引擎

一整套 Unity 6 C# 编码规范。`/u3d` 打底，它本身又建立在 `/coder-c-sharp` 之上。每个主题都是独立技能，智能体只加载当前任务需要的那部分。

| 技能 | 能带来什么 |
|---|---|
| `/u3d-coding` | 统一的 Unity C# 写法，调试时一步步读下来像看故事 |
| `/u3d-naming` ⭐ | 类、资源、文件夹、GameObject 全按同一套规则命名，从此告别 `Hero_final2` |
| `/u3d-common-type-and-suffix` | 每个类、脚本、GameObject 和资源只担一个职责，看后缀就知道它是干什么的 |
| `/u3d-if` | Inspector 字段任由策划调整、改名，存好的数值也不会丢 |
| `/u3d-mb` | 所有 `MonoBehaviour` 都用同一种结构，Inspector 里漏拖的引用启动时就会报出来 |
| `/u3d-so` | 所有 `ScriptableObject` 都用同一种结构，运行时数据只读且始终有效 |
| `/u3d-pfb` | 尽早做成预制体和变体，改一处，所有副本跟着变 |
| `/u3d-game-tuning` | 把游戏数值从代码里搬到策划可编辑的数据中，调平衡不用重新编译 |
| `/u3d-owner-driven-activation` | 临时出现的对象统一交给一个“主人”来生成、显示和隐藏，闲着时零开销 |
| `/u3d-assets-management` | `Assets/` 下每个资源都有固定位置，不用搜也能找到 |


































## 🖋️ 文书

你的学术秘书：引注、笔记、会议纪要、文字修订，样样细致。













### 引注

所有引注都遵循 *Chicago Manual of Style*（芝加哥格式）。从此不用手动排版。

- `/amanuensis-chicago-note` 🌟：生成原生 Markdown 脚注形式的引注
- `/amanuensis-chicago-bibliography`：写参考文献条目，可带注释
- `/assemble-bibliography`：把一篇文档引用过的所有来源整理成一份参考文献
- `/bibliographer`：同时需要脚注和参考文献时，由它统筹上面这几个技能













### 笔记与记录

`/dispositor` 是打底的笔记技能：结构化的笔记，统一的文件名和版式。下面四个专项技能都建立在它之上：

- `/scholiast`：逐段做学术阅读笔记，需要时附上引注
- `/minutes-clerk` ⭐：记会议纪要，每项决议和待办都跟到落实为止
- `/config-writer`：把应用、游戏或系统的设置存成快照，随时可以照着恢复
- `/keybinding-writer`：用简洁的按键符号记录快捷键

另外还有 `/redactor`：帮你修改文字，保留原意和风格，根据你的反馈反复打磨，直到满意为止。


































## 🧱 基础元素

撑起其他所有技能的小部件，小而精确。其他技能会自动调用它们；只想用某条规则时，也可以单独调用。

日期和时间，处处一个格式：

| 技能 | 作用 |
|---|---|
| `/element-dt-year-month-day-format` | 带年份的日期，星期可选 |
| `/element-dt-month-day-format` | 不带年份的日期，星期可选 |
| `/element-dt-time-format` | 24 小时制时间，可以精确到分钟，也可以细到秒的小数位 |
| `/element-dt-watch-day` ⭐ | 30 小时制的“一天”，过了午夜还算今天，夜猫子专用 |
| `/element-dt-watch-week` | 规划用的一周，总是在周日结束 |

还有这些：

- `/element-numerical-values-with-units`：公制和美制单位并列，缩写规范
- `/element-international-phonetic-alphabet`：在难读的词后面标上国际音标，什么语言都行
- `/element-alphabetical-sequence-numbering`：用圆圈字母（ⓐ、ⓑ、ⓒ）标选项，回答时说一个字母就行
- `/element-triage-tags`：`BUG`、`FIXME`、`TODO`、`HACK` 四种标签，各分三档“音量”
- `/sort-and-group-triage-tag`：把文件里已有的标签分组排好，其他内容一概不动


































## 🐙 Git

提交信息值得一读，合并干干净净，并行开发互不打架。

`/working-with-git` 先把规矩立好：没有你点头，智能体绝不推送，也绝不改写历史。在用 Perforce？`/working-with-p4v` 给每个 Perforce 术语都标上对应的 Git 说法，不用在脑子里来回翻译。













### 提交与合并

`/commit-sense` 🌟 让“fix stuff”式的提交成为历史。说一句“commit this”，就能拿到一行精准的摘要，外加逐个文件的改动清单，写清改了什么、为什么改。`/commit-sense-branch-merging` 则负责合并时的提交信息。

分支生命周期的其他环节：

- `/resolve-merge-conflict` ⭐：理顺卡住的合并，两边的改动都兼顾到，冲突标记清理干净
- `/prune-merged-branches`：删掉已经合并的分支，并告诉你删了哪些、留了哪些
- `/submit-pr`：准备好文档，向 `dev` 发起 PR，标题和描述都替你写好













### 用工作树并行开发

三个功能同时开发，谁也不碍着谁。关联工作树就是另开的一个工作目录，有自己的分支。`/tend-linked-wt` 🌟 管它的整个生命周期：用 `/plant-linked-wt` 创建，工作合并后用 `/uproot-linked-wt` 移除。


































## 🤖 智能体

决定智能体怎么和你一轮一轮地配合。`/chat` 定下对话规则：用什么语言回复，对话中各个环节怎么称呼，提问怎么标记才不会被你漏看。













### Movement 与 Suite

大任务得有章法。Suite 指整个多轮任务，Movement 是其中可以单独审阅的一步，小到扫一眼就能判断好坏。`/agent-movement-and-suite` 定义了这两个概念；`/agent-movement-and-suite-with-count` 再把每个 Movement 细分成若干 Count，进度一看就是几分之几。

`/plan-for-suite` 🌟 把这套方法落到实处。智能体不会再一口气改 30 个文件，而是先摸清仓库，写出编号的计划，等你批准后才动手。

- `/execute-plan-for-suite`：每轮只做一个 Movement；进度记在计划文件里，今晚停下，明天接着干，换个会话也没问题
- `/rework-plan-for-suite`：计划跟不上实际情况了？它会先停下来，改好计划，再等你重新批准

节奏你说了算。`/halt-each-movement` 每做完一步就停，等你审阅；`/cascade-all-movements` 把剩下的步骤一口气做完，只有全部完成或需要你拍板时才停。


































## 🪄 元提示词

用来写提示词的提示词。`/write-llm-prompt` ⭐ 把含糊的系统提示词改成真正好用的版本：起草、打分、打磨，JSON schema 等原有结构原样保留。

另外三个技能负责写技能的元数据，也就是告诉智能体什么时候该加载这个技能：

- `/write-skill-description`：写技能的 `description`，开头就点明它做什么
- `/write-skill-when-to-use`：写技能的 `when_to_use`，列出触发说法，并划清适用边界
- `/write-skill-description-and-when-to-use`：两项一起写


































## 📖 术语表

少打几个字，智能体照样懂。每份术语表负责解读一类缩写。

| 技能 | 解读什么 | 示例 |
|---|---|---|
| `/glossary-coder-abbr` | 编程缩写 | `ctor`、`iface`、`mpl` |
| `/glossary-programming-language-codes` | 编程语言代号 | `py`、`ts`、`cpp` |
| `/glossary-natural-language-codes` | 自然语言代号 | `en`、`zh`、`jp` |
| `/glossary-units-of-measure` | 计量单位缩写 | `ft`、`lb`、`mi` |
| `/glossary-element-dt-days-of-week` | 单字母星期代号 | 日期和日程里的星期 |
| `/glossary-secretary-eisenhower-matrix-quadrant` | 艾森豪威尔矩阵的四个象限 | 按重要、紧急划分，附表情符号 |
