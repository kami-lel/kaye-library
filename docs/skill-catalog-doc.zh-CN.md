# Kaye Library：技能目录

[English](skill-catalog-doc.md) | 简体中文

kaye-library 的全部技能都在这里 📚，分组与 [README](../README.zh-CN.md) 保持一致。

用法有两种（比如在 Claude Desktop 里）：

- 手动调用：输入 `/` 加技能名，比如 `/commit-sense`
- 自动触发：直接说出需求，比如“提交一下”，智能体会自己找到对应的技能

刚上手？先试试标 🌟 的首选，再看看标 ⭐ 的推荐。


































## 🤖 智能体

定义智能体如何与你逐轮协作。对话规则自动生效，并以 Kaye 的口吻呈现：回复语言、统一术语、醒目的提问标记。













### Movement 与 Suite

大任务拆成可审阅的小步：智能体先写计划，你批准后，再一次推进一个 **Movement**。从 `/plan-for-suite` 🌟 开始。📖 完整指南：**[Suite 与 Git 使用文档](suite-git-usage-doc.zh-CN.md)**。

先做计划，再动手：

| 技能 | 能带来什么 |
|---|---|
| `/plan-for-suite` 🌟 | 动手前先有一份编号、可审阅的计划；你批准之前什么都不会执行 |
| `/play-suite` | 每轮只做一个 Movement；进度记在计划文件里，今晚停下，明天接着干，换个会话也没问题 |
| `/rework-plan-for-suite` | 计划跟不上变化了？它会先叫停，改好计划，再等你重新批准 |
| `/solo-voice` | 在自己的 instrumental branch 上独立跑完 Suite 中的一个 instrumental Voice，以子智能体或独立会话运行，完成后向主会话汇报；由主会话派发 |

节奏你说了算：

| 技能 | 能带来什么 |
|---|---|
| `/halt-each-movement` | 每做完一个 Movement 就停，等你审阅后再做下一个 |
| `/cascade-all-movements` | 把剩下的 Movement 一口气做完，只有整个 Suite 完成或需要你拍板时才停 |

----

下面两个配套技能负责定义这些概念：

- `/agent-movement-and-suite`：定义 Suite 和 Movement
- `/agent-movement-and-suite-with-count`：把每个 Movement 再拆成若干 Count，进度到了几分之几一目了然
- `/agent-files-and-folders`：新文件用 kebab case、文件夹用 Pascal case 命名，带日期的名称以日期开头；计划文件和文档写作技能会加载它


































## 📝 仓库与项目

项目里的每份文档都写得准确，并且始终跟得上代码。

一个好项目要照顾**五类读者**：README 给访客看，CHANGELOG 告诉用户改了什么，`AGENTS.md` 给 AI 智能体立规矩，`CONTEXT.md` 讲清架构，`docs/` 负责深入细节。可选的 `CREDITS.md` 和 `DEVLOG.md` 分别负责第三方署名和公开的开发日志，尤其适合游戏项目。每份文件都有专门的写作技能。

大多数写作技能都提供两个工作流：**创建**负责从零写出文件，**维护**负责在代码更新后原地同步。

| 文件 | 写给谁 | 写作 | 创建 | 维护 |
|---|---|---|---|---|
| `README.md` | 访客 | `/repo-readme-writer` ⭐ | `/create-readme` | `/maintain-readme` |
| `CHANGELOG.md` | 要升级的用户 | `/repo-changelog-writer` | `/create-changelog` | `/maintain-changelog` |
| `AGENTS.md`（代码仓库） | AI 编程智能体 | `/repo-agents-writer` | `/create-repo-agents` | `/maintain-repo-agents` |
| `AGENTS.md`（任意项目） | AI 智能体 | `/proj-agents-writer` | `/create-project-agents` | `/maintain-project-agents` |
| `CONTEXT.md` | 新加入的开发者和 AI | `/repo-context-writer` | ➖ | ➖ |
| `CREDITS.md` | 被署名的创作者、核查许可证的人 | `/repo-credits-writer` | `/create-credits` | `/maintain-credits` |
| `DEVLOG.md` | 关注开发幕后的人（比如追更游戏或新应用的玩家） | `/repo-devlog-writer` | `/create-devlog` | `/maintain-devlog` |
| `docs/`（代码仓库） | 想深入了解的读者 | `/repo-doc-writer` | `/create-repo-docs` | `/maintain-repo-docs` |
| `docs/`（任意项目） | 想深入了解的读者 | `/proj-doc-writer` | `/create-project-docs` | `/maintain-project-docs` |

`repo-` 系列面向代码仓库，`proj-` 系列什么项目都能用：游戏策划、研究资料、代码库都行。

几个**亮点**：

- `/repo-readme-writer` 能把空荡荡的仓库变成让人愿意读下去的首页，本库的 README 就是这么写出来的
- `/repo-changelog-writer` 遵循 Keep a Changelog 规范，带 `[Unreleased]` 区块和版本链接；`/create-changelog` 甚至能从 Git 历史里重建一份
- `/repo-credits-writer` 为每项第三方素材记一行：路径、来源、作者、许可证，绝不让任何素材不署名就上线
- `/repo-devlog-writer` 把每项改动和促成它的试玩反馈、问卷或 bug 一一对应，配上带说明的截图，数据适合时画成 Mermaid 图表，并如实记录遗留问题
- `/repo-agents-writer` 和 `/repo-context-writer` 让规则和知识各归各位：`AGENTS.md` 写该怎么做，`CONTEXT.md` 写系统怎么运作，个人笔记则放进只属于你自己的 `.local.md` 文件













### 起步与整理

帮新仓库开好头，让文档保持精简，长会话里积累的信息也不会丢。前两个起步技能都遵循 `/repo-structure`：所有目录和顶层文件都按同一套**标准布局**摆放。

| 技能 | 能带来什么 |
|---|---|
| `/initialize-repo` 🌟 | 一次写齐全套**起步文档**：README、CHANGELOG、AGENTS、CONTEXT 和 `docs/`，不重复，不遗漏 |
| `/equip-proj-for-agent` | 只想给智能体立规矩：写好并维护 `AGENTS.md` |
| `/condense-agents-and-context` | 给臃肿的文件瘦身：删掉 `AGENTS.md` 和 `CONTEXT.md` 里已完成的计划和过时内容，只减不增 |
| `/condense-changelog` | 发版前精简 `[Unreleased]`，顺便标出破坏性变更 |
| `/maintenance-before-compact` ⭐ | 在**上下文压缩之前**，把所有长期有效的改动记进 CHANGELOG、AGENTS 和 CONTEXT，积累的信息一点不丢 |













### 合入功能，发布版本

两个工作流，都是合并前做准备、合并后做清理，每次推送或删除都要等你批准：

| 准备 + 合并 + 清理 | 只做准备 | 只做清理 | 合并这一步做什么 |
|---|---|---|---|
| `/land-feature` | `/ready-land-feature` | `/scrub-landed-feature` | 合并到 `dev`，附上清晰的合并信息 |
| `/release-version` ⭐ | `/ready-release-version` | `/scrub-released-version` | 合并到 `main`，打上版本标签 |

📖 逐步讲解：**[合并功能分支](suite-git-usage-doc.zh-CN.md#git-合并功能分支)** 和 **[发布版本](suite-git-usage-doc.zh-CN.md#git-发布版本)**。想走 **PR**？见 [Git](#-git) 分组里的 `/submit-pr`。













### 版本号

上面发版流程的配套技能：

- `/proj-version-extended`：帮你给预发布版本定版本号，比如第二个 beta 是 `1.0.0-beta.2`，第一个候选版本是 `1.0.0-rc.1`，还能附加构建标签
- `/proj-version-title`：根据新旧版本号生成发布标题，比如从 `1.3.2` 升到 `1.4.0`，标题就是 `Minor Release 1.4.0`


































## 🐙 Git

提交信息值得一读，合并干干净净，并行开发互不打架。













在聊天中输入 `g` 提交本次对话的改动，`gi` 提交已暂存的内容，`ig` 全部加入暂存区再提交。📖 每个 Git 技能的完整说明：**[Suite 与 Git 使用文档](suite-git-usage-doc.zh-CN.md#git-规则与提交)**。

| 技能 | 能带来什么 |
|---|---|
| `/commit-sense` 🌟 | 提交时附一行精准摘要和逐文件改动清单，告别“fix stuff” |
| `/commit-sense-branch-merging` | 合并提交的信息也一样讲究 |
| `/resolve-merge-conflict` ⭐ | 理清中断的合并，保留双方意图，并把冲突标记清理干净 |
| `/submit-pr` | 先准备好文档，再向 `dev` 提 PR，标题和描述都替你写好 |
| `/prune-merged-branches` | 删掉已合并的分支，并告诉你删了哪些、留了哪些 |
| `/tend-linked-wt` 🌟 | 管关联工作树的整个生命周期：每个任务独占一个目录，并行开发互不碰撞 |
| `/plant-linked-wt` | 为新任务创建一棵关联工作树 |
| `/uproot-linked-wt` | 工作合并后把它移除 |
| `/working-with-git` | 自动生效：没有你点头，智能体**绝不推送，也绝不改写历史** |
| `/working-with-p4v` | 在用 Perforce？每个术语都标上对应的 Git 说法 |


































## 💻 编程

不管什么语言，代码都干净统一。再也不用替 AI 收拾烂摊子。

一切从 `/coder` 开始，它是所有代码共用的基本规范，比如每行不超过 80 个字符、命名前后一致。一般不用你手动调用：智能体只要写代码，它就会**自动触发**，各语言规范也都建立在它之上。













### 代码体检

一重构，测试就全挂？`/sync-unit-test` 🌟 帮你修正**过时的断言、fixture 和快照**。如果真正出问题的是代码，它会直接指出来，绝不靠改测试把真 bug 糊弄过去。

快发版了？先用 `/review-gaps` ⭐ 把整个仓库过一遍。它会赶在用户之前，把**遗漏、跑偏和没收尾的地方**都找出来，逐个打上标记，等你处理。













### 语言规范

挑你要写的语言就行。大多数规范还会在智能体打开对应文件时自动加载。

| 技能 | 语言 | 能带来什么 |
|---|---|---|
| `/coder-python` ⭐ | Python | 遵循 PEP 8，命名统一，注释讲清意图 |
| `/coder-python-docstring-style` | Python | 默认给每个函数、类和模块配上 Sphinx 风格的 docstring |
| `/coder-python-testing-guidelines` | Python | 按项目自己的约定写 `pytest` 测试 |
| `/coder-c` | C | C99，大括号风格统一 |
| `/coder-cpp` | C++ | 统一的 C++ 风格，以 C 规范为基础 |
| `/coder-ue` | Unreal Engine C++ | Unreal 的编码约定，以 C++ 规范为基础 |
| `/coder-c-sharp` | C# | 统一的大括号风格，配 XML 文档注释 |
| `/coder-javascript-and-typescript` | JavaScript、TypeScript | 以 ES11 为基准，camelCase 命名，配 JSDoc 注释 |
| `/coder-html` | HTML | 规范的 HTML5 结构和语义化标签 |
| `/coder-gdscript` | GDScript | 地道的 Godot 4 写法 |
| `/coder-powershell` | PowerShell | 一套固定的代码风格 |
| `/coder-bash-script` | Bash | 面向 Debian 的脚本、函数和函数库 |
| `/coder-bash-shell` | Bash | 只给单行命令，复制即用 |













### 输出小帮手

三个小技能，专管程序输出的文字：

| 技能 | 能带来什么 |
|---|---|
| `/coder-command-usage-message` | 给 `--help` 和报错信息写简洁的用法说明 |
| `/coder-comment-banner-in-code-comment` | 在源码里用分级横幅注释标出文件标题、章节和小节 |
| `/coder-comment-banner-in-print-out` | 在程序输出里用分级横幅，把日志、演示和测试过程分成清晰的阶段 |


































## 🗓️ 秘书

收件箱、日历、待办、求职，一个**私人助理**全包了。它直接调用智能体已接入的应用来干活。













### 早报与周报

`/good-morning` 🌟 是你的**每日早报**。一条命令清理收件箱、回顾昨天、扫一遍今天的活动、找找招聘机会，最后汇总成**一份报告**。每一步也都能单独用。

`/good-week` 帮你提前看看本周的活动和招聘机会。想给自己打打气？`/recap-yesterday` 和 `/recap-today` 会用一句暖心的话，总结你昨天或今天完成了什么。













### 邮件、日历和待办

`/draft-email` ⭐ 只写你交代的内容，**不添油加醋**，想改几遍改几遍。`/sweep-email-inbox` 把每封未读邮件看一遍、标成已读，再分门别类归好。

日历和待办都是“推”“拉”成对：

| 推到你的应用里 | 拉进对话里 |
|---|---|
| `/push-event-to-calendar`：加一个活动，或者把对话里整理好的一整串活动都加进去 | `/pull-event-from-calendar`：把你的实际日程拉进来 |
| `/push-task-to-gtd`：添加任务，每条都标好所属项目和四象限（艾森豪威尔矩阵） | `/pull-task-from-gtd`：把你的实际待办清单拉进来 |

GTD 是 *Getting Things Done*（中译《搞定》）的缩写，一套经典的任务管理方法。













### 活动和招聘

`/scan-event-radar-daily` 找今天的活动，`/scan-event-radar-weekly` 看未来一周。两者都按 `/secretary-event-brief-format` 的格式输出：标题、关键信息、一段简短概述。`/hunt-job-opportunity` 从各种渠道收集招聘信息，**每个职位一份简报**。


































## 🖋️ 文书

你的**学术秘书**：引注、笔记、会议纪要、文字修订，样样细致。













### 引注

所有引注都遵循 *Chicago Manual of Style*（芝加哥格式）。**从此不用手动排版**。

- `/amanuensis-chicago-note` 🌟：生成原生 Markdown 脚注形式的引注
- `/amanuensis-chicago-bibliography`：写参考文献条目，可带注释
- `/assemble-bibliography`：把一篇文档引用过的所有来源整理成一份参考文献
- `/bibliographer`：同时需要脚注和参考文献时，由它统筹上面这几个技能













### 笔记与记录

`/dispositor` 是打底的**笔记技能**：结构化的笔记，统一的文件名和版式。下面四个专项技能都建立在它之上：

- `/scholiast`：逐段做学术阅读笔记，需要时附上引注
- `/minutes-clerk` ⭐：记会议纪要，每项决议和待办都跟进到落实为止
- `/config-writer`：把应用、游戏或系统的设置存成快照，随时可以照着恢复
- `/keybinding-writer`：用简洁的按键符号记录快捷键

另外还有 `/redactor`：帮你修改润色文字，保留原意和风格，根据你的反馈反复打磨，直到满意为止。


































## 🎮 Unity 引擎

一整套 Unity 6 C# **编码规范**。`/u3d` 打底，它本身又建立在 `/coder-c-sharp` 之上。每个主题都是独立技能，智能体只加载当前任务需要的那部分。

| 技能 | 能带来什么 |
|---|---|
| `/u3d-coding` | 统一的 Unity C# 写法，调试时单步跟下来像读故事一样顺 |
| `/u3d-naming` ⭐ | 类、资源、文件夹、GameObject 全按同一套规则命名，从此告别 `Hero_final2` |
| `/u3d-common-type-and-suffix` | 每个类、脚本、GameObject 和资源只担一个职责，看后缀就知道它是干什么的 |
| `/u3d-if` | Inspector 字段策划可以放心调；字段改名后，已保存的数值也不会丢 |
| `/u3d-mb` | 所有 `MonoBehaviour` 都用同一种结构，Inspector 里漏拖的引用启动时就会报出来 |
| `/u3d-so` | 所有 `ScriptableObject` 都用同一种结构，运行时数据只读且始终有效 |
| `/u3d-pfb` | 尽早做成预制体[Prefab]和变体，改一处，所有实例跟着变 |
| `/u3d-game-tuning` | 把游戏数值从代码里搬到策划可编辑的数据中，调平衡不用重新编译 |
| `/u3d-owner-driven-activation` | 临时出现的对象统一交给一个“主人”来生成、显示和隐藏，闲置时零开销 |
| `/u3d-assets-management` | `Assets/` 下每个资源都有固定位置，不用搜也能找到 |


































## 🪄 元提示词

**用来写提示词的提示词**。`/write-llm-prompt` ⭐ 把含糊的系统提示词改成真正好用的版本：起草、打分、打磨，JSON schema 等原有结构原样保留。

另外三个技能负责写技能的元数据，也就是告诉智能体**什么时候该加载**这个技能：

- `/write-skill-description`：写技能的 `description`，开头就点明它做什么
- `/write-skill-when-to-use`：写技能的 `when_to_use`，列出触发语，并划清适用边界
- `/write-skill-description-and-when-to-use`：两项一起写


































## 🎨 风格

不管写什么，智能体都保持同一种**文风**。

大多数风格技能都是配套技能：其他技能会自动加载它们，一条规则管住所有文档。只有想单独用某条规则时，才需要手动调用。













### Markdown

- `/style-markdown-heading`：标题层级按内容实际嵌套来定，另有跳级的局部标题
- `/style-markdown-list`：短横线列表配 Title Case 标签，表格单元格用速记符号
- `/style-markdown-math`：LaTeX 公式，逐个符号注释
- `/style-markdown-diagrams`：Mermaid 图表与流程图
- `/style-markdown-reference-link`：链接织入点明其主题的句子中
- `/style-markdown-footnotes`：脚注就近放在引用它的文字旁边
- `/style-markdown-endnotes`：所有注释统一作为尾注放在文末
- `/style-markdown-file-assets`：每个文件的图片放进它专属的同级文件夹，如 `CHANGELOG-assets/`，用相对路径链接

长文档要**留白**才好读。`/style-heading-separation` 按标题层级和篇幅长短安排空行；`/style-heading-separation-medium` 和 `/style-heading-separation-long` 则直接套用中篇和长篇的间距。













### 大小写风格

每种风格**单独一个技能**，其他规则引用起来一指一个准。

| 技能 | 风格 | 示例 |
|---|---|---|
| `/style-letter-case-title-case` | 标题式：实词首字母大写，虚词小写 | `The Lord of the Rings` |
| `/style-letter-case-commentary-case` | 注释式：句首小写，句末不加句号 | `check the Config first` |
| `/style-letter-case-snake-case` | 蛇形命名：小写单词用下划线连接 | `total_price` |
| `/style-letter-case-kebab-case` | 短横线命名：小写单词用连字符连接 | `total-price` |
| `/style-letter-case-camel-case` | 小驼峰：首个单词小写，后面每个单词首字母大写 | `totalPrice` |
| `/style-letter-case-pascal-case` | 大驼峰：每个单词首字母大写，不加分隔符 | `TotalPrice` |
| `/style-letter-case-all-caps` | 常量命名：全大写，单词之间用下划线连接 | `TOTAL_PRICE` |













### 文风

两个技能，方向正好相反。`/style-briefness-style` ⭐ 把啰嗦的草稿压缩成**新闻标题式的精简笔记**，适合写状态、摘要和注释。

`/style-good-writing` 则只做**最小改动**的校对：检查拼写、语法、标点和表达是否清楚，原有的语气和用词一概保留。


































## 🧱 基础元素

撑起其他所有技能的**基础积木**，小而精准。它们全是配套技能：其他技能会自动调用，一条规则处处一致。只有想单独用某条规则时，才需要手动调用。

日期和时间，处处同一个格式：

| 技能 | 作用 |
|---|---|
| `/element-dt-year-month-day-format` | 带年份的日期，星期可选 |
| `/element-dt-month-day-format` | 不带年份的日期，星期可选 |
| `/element-dt-time-format` | 24 小时制时间，可以精确到分钟，也可以精确到秒及小数位 |
| `/element-dt-watch-day` ⭐ | 30 小时制的“一天”，过了午夜还算今天，夜猫子专用 |
| `/element-dt-watch-week` | 用于规划的一周，固定以周日结尾 |

还有这些：

- `/element-numerical-values-with-units`：公制和美制单位并列，缩写规范
- `/element-international-phonetic-alphabet`：在难读的词后面标上国际音标，什么语言都行
- `/element-secondary-language-marking`：关键词的第二语言对照放进 `[]`，文档撰写技能会用到它
- `/element-alphabetical-sequence-numbering`：用圆圈字母（ⓐ、ⓑ、ⓒ）标选项，回答时说一个字母就行
- `/element-triage-tags`：`BUG`、`FIXME`、`TODO`、`HACK` 四种标签，每种按大小写分三档“音量”
- `/sort-and-group-triage-tag`：把文件里已有的标签分组排好，其他内容一概不动


































## 📖 术语表

**少打几个字**，智能体照样懂。每份术语表负责解读一类缩写。

它们全是配套技能：其他技能会自动加载，缩写到哪儿都是同一个意思。只有想单独用某套解读时，才需要手动调用。

| 技能 | 解读什么 | 示例 |
|---|---|---|
| `/glossary-coder-abbr` | 编程缩写 | `ctor`、`iface`、`mpl` |
| `/glossary-programming-language-codes` | 编程语言代号 | `py`、`ts`、`cpp` |
| `/glossary-natural-language-codes` | 自然语言代号 | `en`、`zh`、`jp` |
| `/glossary-units-of-measure` | 计量单位缩写 | `ft`、`lb`、`mi` |
| `/glossary-element-dt-days-of-week` | 单字母星期代号 | 日期和日程里的星期 |
| `/glossary-secretary-eisenhower-matrix-quadrant` | 艾森豪威尔矩阵的四个象限 | 按重要、紧急划分，附表情符号 |
