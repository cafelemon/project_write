# Cursor 研究来源清单

> 标注说明：
> - **官方已明确**：可直接作为主结论依据
> - **实践建议**：用于归纳方法，不直接当事实证明
> - **待复核项**：页面跳转、术语变化、可能更新较快，发布前需复核

---

## 一、正文章节 ↔ 来源映射索引

| 正文章节 | 主要来源 | 当前口径 | 备注 |
|---|---|---|---|
| 1. Cursor 是什么，Pro 账号适合谁 | 官网首页、Pricing、Agent Overview | 官方已明确 + 实践建议 | 套餐适合对象属于解释层，不是官方原句 |
| 2. 主要能力与使用入口 | 官网首页、Agent Overview、Prompting Agents、Cloud Agents | 官方已明确 | Cloud Agents 名称历史需注意 |
| 3. Pro 权益、限制、计费 / 额度口径 | Pricing、Models & Pricing、Usage limits | 官方已明确 | **高变动项：pricing / usage** |
| 4. 模型选择策略与适用场景 | Models & Pricing、Available models | 官方已明确 + 实践建议 | **高变动项：models / Max Mode / hidden models** |
| 5. 概念边界（Rules / Skills / Memories / MCP / Hooks / Agent） | Rules、Skills、MCP、Hooks、Agent Overview、memories 跳转验证 | 混合口径 | **高变动项：memories** |
| 6. MCPs | Docs - MCP | 官方已明确 | 配置位置与 transport 以文档为准 |
| 7. Hooks | Docs - Hooks、permissions reference | 官方已明确 + 实践建议 | hook 事件与退出码仍建议发布前抽查 |
| 8. 典型工作流 | Agent Overview、Prompting Agents、Cloud Agents | 实践建议为主 | 用法归纳，不当成官方承诺 |
| 9. 风险与限制 | Pricing、Models & Pricing、MCP、Hooks、permissions | 官方已明确 + 实践建议 | 风险判断有方法论归纳成分 |
| 10. Pro 用户落地建议 | Rules、Skills、MCP、Hooks、permissions | 实践建议为主 | 目录示例与沉淀顺序是作者归纳 |
| 11. 一页结论 | 综述汇总 | 混合口径 | 发布时需确保不把建议写成承诺 |

---

## 二、官方主站 / 定价 / 文档

### 1. Cursor 官网首页
- URL: https://cursor.com/
- 用途：产品定位、能力概览、cloud agents / frontier models 总体表述
- 口径：**官方已明确**

### 2. Pricing
- URL: https://cursor.com/pricing
- 用途：确认 Pro / Pro+ / Ultra / Teams 的套餐差异；确认 Pro 包含 MCPs、skills、hooks、cloud agents
- 口径：**官方已明确**
- 备注：**高频变动页，发布前必复核**

### 3. 文档总览
- URL: https://cursor.com/docs.md
- 用途：总入口；模型、定制化、agent、cloud agents 等导航
- 口径：**官方已明确**

### 4. llms.txt / sitemap
- URL: https://cursor.com/llms.txt
- 用途：快速枚举文档页面、确认帮助中心路径与 docs 路径
- 口径：**官方已明确**

---

## 三、Agent / 模型 / 用量

### 5. Cursor Agent Overview
- URL: https://cursor.com/docs/agent/overview
- 用途：确认 Agent = instructions + tools + model；确认可用工具与 checkpoint / queue 机制
- 口径：**官方已明确**

### 6. Prompting Agents
- URL: https://cursor.com/docs/agent/prompting
- 用途：确认 @ mentions、图像输入、语音输入、模型切换的官方用法
- 口径：**官方已明确**

### 7. Models & Pricing
- URL: https://cursor.com/docs/models-and-pricing
- 用途：确认 usage pools、Auto / Composer / API pool、模型价格表、Max Mode 等
- 口径：**官方已明确**
- 备注：模型清单更新快，属 **高频变动页**

### 8. Help - Usage and limits
- URL: https://cursor.com/help/models-and-usage/usage-limits
- 用途：确认 Pro / Pro Plus / Ultra 每月 API usage 额度，确认月度重置与超额处理
- 口径：**官方已明确**
- 备注：属 **高频变动页**

### 9. Help - Available models
- URL: https://cursor.com/help/models-and-usage/available-models
- 用途：确认 Auto / Premium / Composer 的用户层说明与模型切换方式
- 口径：**官方已明确**
- 备注：属 **高频变动页**

---

## 四、Rules / Skills / 上下文边界

### 10. Docs - Rules
- URL: https://cursor.com/docs/rules
- 用途：确认 Project Rules / User Rules / Team Rules / AGENTS.md 的定义、优先级、适用范围
- 口径：**官方已明确**

### 11. Help - Rules
- URL: https://cursor.com/help/customization/rules
- 用途：确认更偏用户视角的规则说明；强调 rules 只作用于 Agent，不作用于 Tab / Inline Edit
- 口径：**官方已明确**

### 12. Docs - Skills
- URL: https://cursor.com/docs/skills
- 用途：确认 skills 的目录、SKILL.md 格式、自动触发与显式调用、迁移能力
- 口径：**官方已明确**

### 13. Help - Skills
- URL: https://cursor.com/help/customization/skills
- 用途：确认 rules vs skills 的用户层对比
- 口径：**官方已明确**

### 14. Help - Context
- URL: https://cursor.com/help/customization/context
- 用途：确认 @ mentions 的用户说明
- 口径：**官方已明确**

### 15. 关于 memories
- 路径尝试：`https://cursor.com/docs/context/memories`
- 实际跳转：落到 rules 页面
- 用途：验证 memories 是否有独立稳定文档
- 口径：**待复核项**
- 当前判断：发布前需再次检查官方是否提供独立定义页
- 备注：属 **高频变动项**

---

## 五、MCP / Hooks / 权限控制

### 16. Docs - MCP
- URL: https://cursor.com/docs/mcp
- 用途：确认 MCP transport、配置位置、支持能力、OAuth、Config interpolation、安全建议
- 口径：**官方已明确**

### 17. Docs - Hooks
- URL: https://cursor.com/docs/hooks
- 用途：确认 hooks 的事件、配置位置、命令式 / prompt 式 hooks、退出码行为、示例
- 口径：**官方已明确**
- 备注：hook 事件较多，发布前建议抽查一次

### 18. Docs - permissions.json reference
- URL: https://cursor.com/docs/reference/permissions
- 用途：确认 auto-run allowlist、MCP / terminal allowlist、优先级与非安全边界声明
- 口径：**官方已明确**

---

## 六、Cloud Agents

### 19. Docs - Cloud Agents
- URL: https://cursor.com/docs/cloud-agent
- 用途：确认 cloud agents 的入口、模型、MCP 支持、billing、命名历史（Background Agents）
- 口径：**官方已明确**
- 备注：属 **高频变动项**

---

## 七、社区 / 补充资料

### 20. Cursor Forum
- URL: https://forum.cursor.com/
- 用途：作为官方论坛入口，可用于后续补充具体功能讨论与发布变更
- 口径：**待复核 / 补充资料**
- 备注：当前抓取不适合做主证据，更多适合作为后续二次检索入口

### 21. Agent Skills 标准站
- URL: https://agentskills.io
- 用途：辅助理解 skills 为开放标准这一点
- 口径：**补充资料**
- 备注：不应替代 Cursor 官方技能文档本身

---

## 八、本轮写作中采用的事实策略

### A. 可直接下结论的内容
- Pro 套餐包含什么
- 用量池分为 Auto + Composer 与 API pool
- Skills / Rules / MCP / Hooks 的基础定义
- 配置文件位置与典型作用
- Cloud Agents 的基本入口和计费口径

### B. 只做实践归纳、不当成官方承诺的内容
- “默认用 Auto，复杂任务再升模型”的模型路由建议
- “先 Rules 再 Skills 再 MCP 再 Hooks”的建设顺序
- “先观察后阻断”的 Hooks 上线策略
- 目录示例与最小落地配置

### C. 发布前需要复核的点
1. Pro 套餐价格与 API inclusion 数字是否变化
2. 当前模型清单、隐藏模型、Max Mode 规则是否变化
3. memories 是否有了独立官方文档
4. cloud agents 对个人 Pro 的具体可用边界是否更新
5. 官方是否继续沿用“Premium”这一帮助中心表述，还是已被新的 UI 术语替换
