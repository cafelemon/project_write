# Cursor Pro 研究指南

> 目标：基于 **Cursor Pro 个人账号** 视角，梳理 Cursor 的核心能力、使用方式、模型选择、rules / skills / memories / MCP / hooks 等概念边界，并给出可执行建议。
>
> 口径说明：
> - **官方已明确**：Cursor 官网、Docs、Help、Pricing 页面已明确写出
> - **实践建议**：基于官方能力边界整理出的推荐用法
> - **待复核项**：官方术语存在跳转、改名、页面不完整或易误解之处，发布前建议再次核验

---

## 1. Cursor 是什么，Pro 账号适合谁

### 1.1 产品定位
**官方已明确**：Cursor 是一个 **AI editor and coding agent**。它不仅是聊天助手，还能结合代码库搜索、文件读写、终端、浏览器、MCP 工具等能力，执行较完整的软件开发任务。

### 1.2 套餐边界摘要
**官方已明确 + 实践建议**：当前写作以官方 Pricing / Help 可确认信息为基础，主文只把套餐差异讲到“如何影响个人使用决策”的粒度。

| 套餐 | 适合对象 | 核心价值 | 重点能力 | 不要期待什么 |
|---|---|---|---|---|
| Hobby / 免费 | 低频体验者、仅想试试编辑器 AI 能力的人 | 低门槛试用 Cursor 的基本工作流 | 基础补全、有限 Agent 体验、基础模型入口 | 不要期待高强度 Agent 使用、完整高级能力、长期主力开发体验 |
| Pro | 个人开发者、独立开发者、技术负责人、重度 AI 编程用户 | 以个人成本拿到较完整的 agentic coding 能力闭环 | 更高 Agent 用量、frontier models、MCPs、skills、hooks、cloud agents | 不要期待团队级统一治理、组织报表、强共享策略和企业管控 |
| Teams / Enterprise | 需要多人协作、规则共享、组织治理与审计的团队 | 从“个人效率工具”升级为“团队协作与治理平台” | 团队规则、共享配置、组织级权限/治理/报表（以官方当前套餐页为准） | 不要把它理解成单纯更大个人额度；价值重点不是只多给一点 token |

### 1.3 本任务为何以 Pro 为主
**实践建议**：本研究以 Pro 为主，而不是平均展开所有套餐，原因有三：
1. Pro 是个人用户最容易形成“完整闭环”的分界点：已经覆盖 Agent、模型、MCP、skills、hooks、cloud agents 等关键能力。
2. 如果以 Hobby 为主，很多机制只能点到为止，无法讲清实际落地方法。
3. 如果以 Teams / Enterprise 为主，主题会明显偏向团队治理、共享规则、组织控制，不再适合作为个人研究主线。

### 1.4 Pro 账号适合谁
**官方已明确 + 实践建议**：Pro 更适合以下人群：
- 个人开发者、独立开发者、技术负责人
- 高频使用 Agent、需要访问前沿模型的人
- 希望在本地编辑器内完成“理解代码 -> 改代码 -> 跑命令 -> 验证结果”闭环的人
- 需要试用 MCP、skills、hooks、cloud agents 等高级能力的人

**不那么适合**：
- 仅偶尔体验 AI 补全的人，Hobby 可能已足够
- 需要团队级统一治理、团队规则强制、组织分析报表的人，这类更偏 Teams / Enterprise

---

## 2. 主要能力与使用入口

### 2.1 主要能力总览
**官方已明确**：Cursor 的 Agent 由三部分组成：
1. **Instructions**：系统提示 + rules
2. **Tools**：文件编辑、代码搜索、终端、浏览器、MCP 等
3. **Model**：所选模型

### 2.2 常见使用入口
**官方已明确**：
- **Agent Chat / 侧边栏**：复杂任务主入口
- **Inline Edit / Cmd/Ctrl+K**：针对局部代码的编辑
- **Tab**：行内补全
- **Cloud Agents**：云端并行执行任务
- **Web / Slack / GitHub / Linear**：触发 cloud agents 的外部入口

### 2.3 Pro 用户最常用的能力组合
**实践建议**：
- 日常开发：Agent + Auto / Composer
- 中等复杂改动：Agent + 指定模型 + Rules
- 外部系统联动：Agent + MCP
- 自动化治理：Agent + Hooks
- 长任务/并行任务：Cloud Agents

---

## 3. Pro 权益、限制、计费 / 额度口径

### 3.1 Pro 官方权益
**官方已明确**：Pro 价格页显示 Pro（$20/月）包含：
- 相比 Hobby 更高的 Agent 使用额度
- 访问 frontier models
- MCPs、skills、hooks
- Cloud agents

### 3.2 Pro 的 usage 口径
**官方已明确**：个人计划存在两类 usage pool：
- **Auto + Composer pool**：适合日常 agentic coding，包含更多内置使用量
- **API pool**：选择具体模型时，按模型 API 价格消耗；个人计划至少含 **$20/月 API usage**

**官方已明确**：Help 页面写明：
- **Pro ($20/mo)**：$20 的 API agent usage + generous Auto / Composer usage
- 用量按月重置，不结转
- 超额后可启用按量付费（on-demand usage）或升级套餐

### 3.3 模型费用口径
**官方已明确**：
- Auto 有固定 token 费率
- Premium / 指定模型按对应模型 API 价格计费
- 个人计划使用 **Max Mode** 时，在模型 API rate 基础上会有 **20% 上浮**

### 3.4 Pro 用户应如何理解“够不够用”
**实践建议**：
- 若主要用 Auto / Composer 做日常编码，Pro 通常足够起步
- 若频繁指定 Claude Opus、GPT-5 Codex、长上下文模型，$20 API pool 会消耗更快
- 若长期把 Cursor 当主力 agent 平台，通常需要：
  1. 管理模型切换习惯
  2. 控制 Max Mode 使用场景
  3. 必要时开启 on-demand usage

### 3.5 待复核点
- **待复核项**：官方 pricing / docs 会动态变化，模型清单、费率、是否 hidden by default、Max Mode 支持情况应以发布当天页面为准

---

## 4. 模型选择策略与适用场景

### 4.1 官方模型选择口径
**官方已明确**：
- **Auto**：平衡智能、成本、可靠性，适合 everyday tasks
- **Premium / 指定高能力模型**：更偏能力优先，适合复杂任务
- **Composer**：Cursor 自研模型，强调交互式编码
- Claude Opus / GPT Codex 一类模型更适合复杂多步任务

### 4.2 Pro 视角的场景化模型选择表
**实践建议**：把模型选择从“凭感觉切换”改成“按任务档位路由”。

| 场景 | 推荐 | 备选 | 何时升级 | 成本提醒 |
|---|---|---|---|---|
| 读代码、找文件、理解局部逻辑 | Auto | Composer | 如果连续多轮都答不准、定位不稳，再升高能力模型 | 这是最适合长期默认档的场景，尽量别一开始就上昂贵模型 |
| 小步改动、补测试、修简单 bug | Auto | Composer | 当涉及跨 3 个以上模块或多轮修改仍反复出错时升级 | 常规任务优先控制在 Auto / Composer，避免无谓消耗 API pool |
| 高频对话式编码、边试边改 | Composer | Auto | 当需要更强规划能力或复杂推理时升级到高能力模型 | Composer 适合高频迭代，但也不应代替所有复杂分析 |
| 方案设计、跨模块重构、复杂调试 | 高能力模型（Claude / GPT Codex 类） | Auto 先做预分析，再切高能力模型 | 当任务涉及架构决策、复杂依赖链、长链路排障时直接升级 | 复杂模型消耗明显更快，先缩小范围再调用更划算 |
| 大仓理解、长上下文、多文件链路排查 | 长上下文 / Max Mode（必要时） | 高能力模型 + 手工缩上下文 | 当普通高能力模型因上下文不足无法稳定处理时再升 | 这是最容易打穿 Pro API pool 的场景；先搜索、@mentions、rules 压缩上下文 |
| 外部系统联动、MCP 多工具任务 | Auto 或 Composer 起步 | 高能力模型 | 当工具调用链复杂、需要同时规划多步外部操作时升级 | 真正贵的不只是模型，还是反复试错带来的轮次与工具调用 |

### 4.3 一套可执行的模型路由建议
**实践建议**：
- 第 1 档：**Auto** 处理大部分常规工作
- 第 2 档：**Composer** 处理高频开发迭代
- 第 3 档：**高能力模型** 处理关键难题
- 第 4 档：**Max Mode / 长上下文** 只在确有必要时开启

### 4.4 何时不要急着升级模型
**实践建议**：以下情况优先补上下文，而不是直接换更贵模型：
- 需求本身没写清楚
- 没有用 `@文件` / `@符号` / 搜索缩小范围
- 项目规范没有沉淀到 rules / AGENTS.md
- 当前任务实际是流程不清，而不是模型不够强

---

## 5. 概念边界：rules / skills / memories / project 级约束 / agents

这一部分是最容易混淆的。

### 5.1 核心概念边界对照表

| 名称 | 主要作用 | 存放位置 / 配置位置 | 是否持久化 | 是否项目级 | 主要属于哪类 | 与相邻概念的区别 |
|---|---|---|---|---|---|---|
| Rules | 给 Agent 的持久化约束与行为指令 | 用户级规则、项目级规则、团队级规则等规则入口 | 是 | 可全局也可项目级 | 约束 | 是“长期规则层”，不是一次性提示词，也不是工具接入层 |
| Project Rules | 把项目规范、目录规则、编码要求固化到仓库内 | `.cursor/rules/` | 是 | 是 | 约束 | 是 Rules 的项目级子集；比 AGENTS.md 更结构化，可按范围 / 触发条件生效 |
| AGENTS.md | 用 markdown 写的轻量项目说明与 Agent 指令 | 仓库根目录或项目约定位置的 `AGENTS.md` | 是 | 是 | 约束 / 流程 | 更轻、更直接；但不如 Project Rules 适合做精细匹配和规则元数据 |
| Skills | 封装可复用的多步骤工作流 | `.cursor/skills/`、`.agents/skills/`、`~/.cursor/skills/` | 是 | 可项目级也可全局 | 流程 | 强调“怎么做一类任务”；区别于 Rules 的“长期约束” |
| Memories | 保留某种持续性上下文或偏好线索 | 官方独立稳定入口当前仍待复核 | 待复核 | 待复核 | 约束 / 上下文 | 目前不宜把它当成与 rules / skills 同等级、可明确落地的文件系统机制 |
| MCP | 给 Cursor 接入外部工具与数据源 | `.cursor/mcp.json`、`~/.cursor/mcp.json` | 是 | 可项目级也可全局 | 工具 | 解决“能调用什么外部能力”，不负责项目规范，也不是执行阻断机制 |
| Hooks | 在 agent loop 各阶段观察、提醒、阻断、扩展行为 | `.cursor/hooks.json`、`~/.cursor/hooks.json` | 是 | 可项目级也可全局 | 控制 | 解决“何时拦、何时记、何时注入”；区别于 MCP 的工具接入，区别于 Rules 的静态约束 |
| Agent | Cursor 的主执行体，负责理解指令、调用工具、产出结果 | 产品运行时主体 | 运行时存在 | 可作用于任一项目 | 执行体 | Agent 是“干活的人”；Rules / Skills / MCP / Hooks 都是在影响它如何干活 |
| Subagent | Agent 为特定任务拆分出的子执行体 | 产品运行时 / Cloud Agent / 内建或自定义子代理机制 | 运行时存在 | 通常跟随当前任务或项目 | 执行体 | 是 Agent 的任务拆分与并行化形态，不等于 rules/skills，也不是新的配置文件类别 |

### 5.2 Rules 是什么
**官方已明确**：Rules 是给 Agent 的持久化指令，用来反复施加项目规范、风格、流程要求。

规则类型包括：
- **Project Rules**：`.cursor/rules/`，项目级、可版本控制
- **User Rules**：用户全局偏好，跨项目生效
- **Team Rules**：团队级，仅 Teams / Enterprise 主线支持
- **AGENTS.md**：更轻量的 markdown 指令文件

**关键边界**：
- Rules 主要作用于 **Agent (Chat)**
- **不影响 Tab**
- User Rules **不作用于 Inline Edit (Cmd/Ctrl+K)**

### 5.3 Skills 是什么
**官方已明确**：Skills 是可复用的、可移植的、版本化的任务能力包，适合 **多步骤工作流**。

典型特点：
- 存在于 `.agents/skills/`、`.cursor/skills/`、`~/.cursor/skills/`
- 以文件夹 + `SKILL.md` 的形式组织
- 可包含 `scripts/`、`references/`、`assets/`
- 既可自动被 Agent 判断使用，也可通过 `/skill-name` 显式调用

**关键边界**：
- Rules 更像“持续约束”
- Skills 更像“可复用流程包”

### 5.4 AGENTS.md 是什么
**官方已明确**：AGENTS.md 是比 `.cursor/rules/` 更轻量的 agent 指令承载方式。

**关键边界**：
- AGENTS.md 更像简单项目说明书
- `.cursor/rules/` 支持更细的触发条件和元数据
- 若需要 path/glob / intelligent apply / manual apply，优先用 rules

### 5.5 Memories 是什么
**待复核项**：当前官方文档抓取中，`memories` 路径跳转到了 rules 页面，说明文档路由或术语可能仍在调整。

**当前谨慎口径**：
- 不建议在本版文档中把 memories 写成与 rules / skills 等价的成熟文件系统能力
- 若发布时仍无稳定官方独立文档，应把 memory 表述为：**Cursor 可能通过历史对话、past chats、上下文系统保留部分延续性，但持久项目规范的主载体仍应视为 rules / AGENTS.md / skills**

### 5.6 Project 级约束到底放哪里
**实践建议**：
- 简单项目约束：`AGENTS.md`
- 需要精细匹配、按文件生效：`.cursor/rules/`
- 需要分步骤流程：`.cursor/skills/`
- 需要外部工具授权边界：`permissions.json` 与 MCP / hooks 配置

### 5.7 Agents / Subagents 是什么
**官方已明确**：Agent 是 Cursor 的主执行体；部分内建 subagents 会自动选模型；自定义 subagents 可继承父模型或指定 `fast` / 特定模型。

**关键边界**：
- “Agent” 是执行框架
- “Rules / Skills / Hooks / MCP” 是给 Agent 提供约束、流程、工具、控制点的不同机制
- 不应把这些概念混成“提示词的别名”

---

## 6. MCPs

### 6.1 MCP 是什么
**官方已明确**：MCP（Model Context Protocol）让 Cursor 接入外部工具与数据源。

### 6.2 支持的方式
**官方已明确**：Cursor 支持三种 transport：
- `stdio`
- `SSE`
- `Streamable HTTP`

支持能力包括：
- Tools
- Prompts
- Resources
- Roots
- Elicitation
- Apps 扩展

### 6.3 配置位置
**官方已明确**：
- 项目级：`.cursor/mcp.json`
- 全局级：`~/.cursor/mcp.json`

### 6.4 Pro 用户如何使用 MCP
**实践建议**：
- 先从只读工具开始：文档检索、issue 查询、设计稿读取
- 再逐步扩展到写操作：创建任务、更新 ticket、调用内部 API
- 配合 approval / allowlist 控制风险

### 6.5 安全建议
**官方已明确 + 实践建议**：
- 只安装可信来源的 MCP server
- 不把高权限 token 硬编码进 `mcp.json`
- 优先用环境变量注入密钥
- 涉及敏感系统时优先本地 `stdio`
- 为高风险 server 做最小权限配置

### 6.6 Pro 视角的适用场景
- GitHub / GitLab 协作
- Linear / Jira / Notion / Figma 等研发上下游联动
- 内部知识库、文档库、API 网关接入
- 测试平台、日志平台、观测平台接入

---

## 7. Hooks

### 7.1 Hooks 是什么
**官方已明确**：Hooks 用自定义脚本观察、控制、扩展 agent loop。它们通过 stdio 传递 JSON，可在阶段前后执行、阻断或修改行为。

### 7.2 支持的事件（示例）
**官方已明确**：
- `sessionStart` / `sessionEnd`
- `preToolUse` / `postToolUse`
- `beforeShellExecution` / `afterShellExecution`
- `beforeMCPExecution` / `afterMCPExecution`
- `beforeReadFile` / `afterFileEdit`
- `beforeSubmitPrompt`
- `subagentStart` / `subagentStop`
- `preCompact`
- `stop`
- Tab 专用：`beforeTabFileRead` / `afterTabFileEdit`

### 7.3 配置位置
**官方已明确**：
- 项目级：`<project>/.cursor/hooks.json`
- 全局级：`~/.cursor/hooks.json`

### 7.4 Hook 的典型用途
**官方已明确 + 实践建议**：
- 编辑后自动格式化
- 记录 agent 审计日志
- 检测敏感信息 / secrets / PII
- 阻断危险 shell 命令
- 对 MCP 调用加审批
- 会话启动时注入上下文

### 7.5 Pro 用户应该怎么上 hooks
**实践建议**：
1. 第一步只做 **可观察**：记录日志，不阻断
2. 第二步再做 **软提醒**：高风险命令 ask
3. 第三步再做 **硬阻断**：生产 SQL、危险删除、敏感网络写操作 deny

### 7.6 风险提醒
**实践建议**：
- Hook 太多会影响体验和稳定性
- fail-open / exit code 行为要看清楚
- 脚本本身也是代码，需要测试与版本控制

---

## 8. 典型工作流（Pro 账号视角）

### 工作流 A：日常开发
1. 使用 Auto / Composer 打开 Agent
2. 用自然语言描述需求
3. 必要时用 `@文件`、`@符号` 补上下文
4. 让 Agent 读代码、改代码、跑测试
5. 用 checkpoints 或 Git 审核变更

### 工作流 B：复杂需求拆解
1. 先让 Agent 产出方案 / 计划
2. 再切到更强模型做实现
3. 用 Rules 约束编码规范
4. 必要时把重复流程沉淀成 Skill

### 工作流 C：外部系统联动开发
1. 配置 MCP server
2. 在任务中让 Agent 自动调用外部工具
3. 用 hooks 和 permissions 控制自动执行边界
4. 审核结果再合并

### 工作流 D：高风险仓库治理
1. 项目内编写 `AGENTS.md` + `.cursor/rules/`
2. 配置 hooks 审核 shell / MCP 行为
3. 必要时限制 auto-run allowlist
4. 把高频流程封装成 skills

### 工作流 E：并行任务
1. 需要长时间运行或并行执行时，使用 cloud agents
2. 控制 spend limit
3. 让本地 Cursor 处理审查与收尾

---

## 9. 风险与限制

### 9.1 成本风险
**官方已明确 + 实践建议**：指定昂贵模型、长上下文、Max Mode、Cloud Agents 都可能迅速拉高消耗。

### 9.2 权限风险
MCP、终端、hooks、cloud agents 都可能触达外部系统或执行真实操作。Pro 用户虽然能用高级能力，但也更需要最小权限原则。

### 9.3 规则误用风险
Rules、skills、hooks 都能“影响 agent 行为”，但作用层级不同；混用不当会导致：
- 重复约束
- 指令冲突
- 调试困难

### 9.4 认知偏差风险
不要把“Cursor 会一点历史记忆/上下文延续”误解为“它天然理解项目规范”。真正可复用、可审计、可迁移的项目知识，仍应沉淀到 rules / AGENTS.md / skills 中。

### 9.5 文档演进风险
Cursor 近期能力迭代较快，部分页面存在重定向、路径改名、帮助中心与 docs 口径并存情况，发布前应二次校验。

---

## 10. Pro 用户落地建议

### 10.1 最小可用配置
建议一个 Pro 用户至少建立：
- `AGENTS.md`：项目基本规范
- `.cursor/rules/`：2~5 条高价值规则
- `.cursor/skills/`：1~3 个高频工作流 skill
- `.cursor/mcp.json`：只接最需要的外部工具
- `.cursor/hooks.json`：先做日志和审批，不急着全自动

### 10.2 最小落地目录示例

```text
project-root/
├─ AGENTS.md
├─ .cursor/
│  ├─ rules/
│  │  ├─ coding-style.mdc
│  │  └─ testing.mdc
│  ├─ skills/
│  │  └─ bugfix/
│  │     └─ SKILL.md
│  ├─ mcp.json
│  └─ hooks.json
```

- `AGENTS.md`：放最基础、所有人一眼能看懂的项目协作说明与 Agent 指令
- `.cursor/rules/`：放结构化项目规则，适合按目录、文件类型、场景精细生效
- `.cursor/skills/`：放高频可复用流程，例如 bugfix、code-review、release-check
- `.cursor/mcp.json`：声明项目需要接入的外部工具与数据源
- `.cursor/hooks.json`：声明哪些阶段需要记录、提醒、审批或阻断

### 10.3 推荐沉淀顺序
1. 先把规则写清楚
2. 再把高频流程做成 skills
3. 再接 MCP
4. 最后再上 hooks 和 auto-run allowlist

### 10.4 何时应该升级而不是继续硬控 Pro
**实践建议**：
- 多人协作需要共享规则和集中治理
- 需要组织级报表和权限控制
- 高强度使用导致 Pro usage 长期吃紧

这时应评估 Teams / Enterprise，而不是只靠 Pro 叠技巧。

---

## 11. 一页结论

### 11.1 对 Pro 用户最重要的判断
- **Cursor Pro 不是“更高级补全”，而是“可运行的个人级 AI 开发工作台”**
- 真正的效率提升不只来自模型，而来自 **模型 + rules + skills + MCP + hooks** 的组合
- Pro 的关键不是“能不能用”，而是“如何把额度、权限、流程治理用得平衡”

### 11.2 推荐默认打法
- 默认模型：**Auto**
- 项目规范：**AGENTS.md + Project Rules**
- 重复流程：**Skills**
- 外部集成：**MCP**
- 风险控制：**Hooks + permissions.json**
- 高价值长任务：**Cloud Agents**

---

## 12. 待 review 重点
- Pro 权益与 usage 数字是否需在发布当天重新核对
- memories 的保守表述是否足够稳妥，是否仍需继续单列为待复核边界项
- Teams / Enterprise 的边界摘要是否与当前官方套餐页完全一致
- hooks / permissions / auto-run 的关系是否需要单独画一张执行链路图
