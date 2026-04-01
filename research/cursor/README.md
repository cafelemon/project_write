# Cursor 研究套件

> 面向 **Cursor 个人 Pro 账号主视角** 的中文研究与落地文档。本文档集用于回答三个问题：
> 1. Cursor 到底是什么、适合谁、边界在哪里
> 2. 个人 Pro 用户该如何把 Agent、Rules、Skills、MCP、Hooks 用成稳定工作流
> 3. 发布前哪些信息可直接采信，哪些必须二次复核

---

## 1. 这套文档解决什么问题

这不是单篇说明文，而是一套围绕 **“个人开发者如何把 Cursor 用到可持续、可治理、可复用”** 组织的研究包。

当前套件重点覆盖：
- Cursor 的产品定位与 Pro 主线能力
- Rules / AGENTS.md / Skills / Memories / MCP / Hooks / Agent 的概念边界
- Pro 用户最常见的模型选择、成本控制与落地顺序
- 可直接复用的提示词模板
- 各结论对应的来源与待复核点

## 2. 文档结构分层

### 第一层：总览与导航
- `README.md`：总入口页，说明文档层次、推荐阅读顺序、文档关系、最小校验清单

### 第二层：主体研究文档
- `cursor-guide.md`：主文档；回答“Cursor 是什么、怎么选套餐、怎么选模型、各机制边界是什么、如何落地”

### 第三层：操作模板
- `cursor-prompt-templates.md`：面向 Cursor Agent 的提示词模板；回答“拿到具体任务后怎么发指令更稳”

### 第四层：证据与复核层
- `sources.md`：来源清单、章节映射、口径标注、待复核项；回答“每条结论依据哪里、哪些地方别说死”

## 3. 推荐阅读顺序

### 读法 A：第一次了解 Cursor
1. 先看 `cursor-guide.md` 第 1～3 节：产品定位、套餐边界、Pro 主视角
2. 再看第 4～7 节：模型、概念边界、MCP、Hooks
3. 最后看 `cursor-prompt-templates.md`：把研究结论转成实际使用动作

### 读法 B：已经在用 Cursor，想补治理与边界
1. 先看 `cursor-guide.md` 第 5 节“核心概念边界对照表”
2. 再看第 10 节“最小落地配置 / 目录示例 / 沉淀顺序”
3. 最后到 `sources.md` 检查高变动信息是否需要重新核验

### 读法 C：准备发布或对外分享
1. 通读 `cursor-guide.md`
2. 对照 `sources.md` 完成高变动项复核
3. 用 `cursor-prompt-templates.md` 选出适合示例展示的模板

## 4. 文档之间的关系

- `cursor-guide.md` 是 **主线叙述**：给出完整认知框架与可执行建议
- `cursor-prompt-templates.md` 是 **动作层补充**：把主线中的方法论变成可复制输入
- `sources.md` 是 **证据层与风控层**：为主文档提供出处，并标明哪些内容需要发布前复核
- `README.md` 是 **导航层**：帮助读者快速进入正确阅读路径，而不是把所有判断塞在首页

## 5. 与 codex 套件的对齐关系

本套件刻意与既有 **codex 套件** 保持同级结构和相似使用方式，便于横向比较与后续整合：

| 维度 | Cursor 套件 | codex 套件 | 当前对齐情况 |
|---|---|---|---|
| 总入口页 | `README.md` | codex 对应入口文档 | 已对齐 |
| 主研究文档 | `cursor-guide.md` | codex 主指南 | 已对齐 |
| 提示词模板 | `cursor-prompt-templates.md` | codex 模板集 | 已对齐 |
| 来源清单 | `sources.md` | codex sources / references | 已对齐 |
| 团队导读 / SOP | 尚未单列 | codex 若已有团队导读或 SOP | **暂未覆盖** |
| 组织级治理专题 | 仅简述 Teams / Enterprise 边界 | codex 若已有更完整治理材料 | **暂未完全对齐** |

### 当前未覆盖项
本轮仍以 **个人 Pro 主视角** 收口，因此以下内容若要完全对齐 codex 套件，建议后续单独补篇：
- 团队导读版（面向技术负责人 / 团队管理员）
- 组织级 SOP（权限、审批、成本、审计、共享规则）
- 与 codex / Claude Code / OpenAI Codex 的横向选型对照页

## 6. 这套内容的使用边界

- **主线口径**：以 Cursor 官方站、Docs、Help、Pricing 可确认信息为准
- **实践建议**：用于落地方法，不当成官方承诺
- **高变动项**：pricing、models、memories、cloud agents 等发布前必须再复核

## 7. 发布前最小校验清单

对外发布前，至少做这几项最小校验：

- [ ] Pricing 页面是否仍能确认当前套餐名称、价格、包含项
- [ ] models & pricing / available models 页面是否仍支持文中提到的模型口径
- [ ] memories 是否仍无稳定独立文档，若有需更新表述
- [ ] cloud agents 的个人 Pro 可用边界是否有变更
- [ ] 主文中的“官方已明确 / 实践建议 / 待复核项”标注是否仍准确
- [ ] README、主指南、模板、sources 之间术语是否一致

## 8. 快速进入

- 想建立完整认知：看 [`cursor-guide.md`](./cursor-guide.md)
- 想直接拿模板开始用：看 [`cursor-prompt-templates.md`](./cursor-prompt-templates.md)
- 想核对事实依据：看 [`sources.md`](./sources.md)
