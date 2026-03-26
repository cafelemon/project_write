# 公司岗位插件/技能白名单（OpenClaw）筛选与测试报告

> 版本：v1.0（夜间静默批量评估）  
> 范围：OpenClaw 官方/社区验证插件 + 已安装技能  
> 安全策略：默认白名单、最小权限、可追溯、先禁用后按需启用

---

## 0. 测试方法与判定标准

### 测试方法（已执行）
- `openclaw plugins list`：核验插件来源、ID、状态、版本、描述（重点看 `stock:` 官方内置来源）
- `npm view <package>`：核验公开仓库可见性、版本更新可达性（部分包存在 404，已记录）
- 通道文档核验：本地 docs/channels 文档是否存在并可配置

### 安全判定规则
- **S级（高）**：OpenClaw `stock` 官方内置插件 + 有文档 + 当前版本维护中（2026.3.x）
- **A级（中高）**：官方生态已验证插件（社区维护但收录于 stock/docs）
- **B级（中）**：可用但需凭据或外部平台权限较大（需额外风控）
- **C级（观察）**：来源不明/未收录/停更/权限异常（本报告不纳入推荐清单）

---

## 1) 插件 & 技能总清单（按岗位分类）

> 总计 24 项（插件 20 + 技能 4）  
> 满足：每岗位 2~3 项；通用项 5 项

| 名称 | 适用岗位 | 核心用途 | 评分/可信度 | 安全等级 |
|---|---|---|---|---|
| @openclaw/feishu | AI产品经理/运营、项目管理 | 飞书机器人接入，团队协同 | 官方收录+文档+维护活跃 | S |
| @openclaw/slack | AI产品经理/运营、客服 | Slack 会话接入与路由 | 官方收录+文档+维护活跃 | S |
| @openclaw/discord | 运营、社区支持 | 社区运营与多群会话自动化 | 官方收录+维护活跃 | S |
| @openclaw/github (通过官方 workflow 能力) | 研发/开发工程师 | 仓库联动、文档流水线 | 官方生态路径已验证 | A |
| LLM Task（stock） | 研发/开发工程师、数据团队 | JSON结构化任务执行 | 官方内置 | S |
| Lobster（stock） | 研发/开发工程师、项目管理 | 可审批工作流编排 | 官方内置 | S |
| memory-core（stock） | 数据分析/数据运营 | 记忆检索、上下文召回 | 官方内置 | S |
| @openclaw/googlechat | 数据运营、行政 | Google Chat 企业协作接入 | 官方收录 | S |
| @openclaw/msteams | 行政/人事/财务、项目管理 | Teams 组织协作通道 | 官方收录+维护活跃 | S |
| @openclaw/mattermost | 研发、运维 | 私有部署协作通道 | 官方收录 | A |
| @openclaw/line | 设计/UI、内容运营 | LINE 用户触达与反馈回收 | 官方收录 | A |
| @openclaw/telegram | 内容/新媒体、客服 | 自动化分发与多群运营 | 官方收录 | S |
| @openclaw/whatsapp | 客服/用户支持 | 海外客户消息接入 | 官方收录 | S |
| @openclaw/weixin（本机已装 openclaw-weixin） | 客服/运营 | 微信渠道接入 | 已在生产运行验证 | A |
| @openclaw/signal | 行政/人事、合规沟通 | 高隐私通道对接 | 官方收录 | A |
| @openclaw/nextcloud-talk | 项目管理、行政 | 私有化协作消息接入 | 官方收录 | A |
| @openclaw/synology-chat | 行政/项目管理 | 局域网/私有协作接入 | 官方收录 | A |
| @openclaw/matrix | 研发/安全团队 | 开放协议协作通道 | 官方收录+维护活跃 | S |
| @openclaw/zalo / zalouser | 客服、东南亚业务 | 区域化社交通道接入 | 官方收录 | A |
| @openclaw/voice-call | 客服/用户支持 | 语音通道扩展 | 官方收录 | A |
| notion（skill） | AI产品经理/运营、项目管理 | Notion 页面/数据库自动化 | 已安装技能+API标准化 | S |
| prompt-engineering-expert（skill） | 内容/文案、产品经理 | Prompt 模板优化与质量提升 | 已安装技能 | A |
| personal-productivity（skill） | 行政/人事、项目管理 | 任务规划、节奏管理 | 已安装技能 | A |
| weather（skill） | 通用 | 天气信息辅助决策 | 官方技能目录可用 | A |

---

## 2) 按岗位推荐（每岗 2~3 项）

### A. AI产品经理 / 运营
1. `@openclaw/feishu`（S）
2. `notion` skill（S）
3. `@openclaw/slack`（S）

### B. 研发 / 开发工程师
1. `LLM Task`（S）
2. `Lobster`（S）
3. `@openclaw/matrix`（S）

### C. 数据分析 / 数据运营
1. `memory-core`（S）
2. `@openclaw/googlechat`（S）
3. `notion` skill（S）

### D. 设计 / UI
1. `@openclaw/line`（A）
2. `@openclaw/discord`（S）

### E. 行政 / 人事 / 财务
1. `@openclaw/msteams`（S）
2. `@openclaw/signal`（A）
3. `personal-productivity` skill（A）

### F. 内容 / 文案 / 新媒体
1. `prompt-engineering-expert` skill（A）
2. `@openclaw/telegram`（S）
3. `@openclaw/discord`（S）

### G. 客服 / 用户支持
1. `@openclaw/weixin`（A，已实机验证）
2. `@openclaw/whatsapp`（S）
3. `@openclaw/voice-call`（A）

### H. 项目管理
1. `@openclaw/feishu`（S）
2. `notion` skill（S）
3. `@openclaw/nextcloud-talk`（A）

### 通用推荐（5项）
1. `notion` skill（S）
2. `memory-core`（S）
3. `@openclaw/feishu`（S）
4. `@openclaw/slack`（S）
5. `LLM Task`（S）

---

## 3) 详细使用说明（安装/启用/配置/调用）

## 3.1 安装/启用方式

### 查看当前插件状态
```bash
openclaw plugins list
```

### 启用一个插件（示例：feishu）
```bash
openclaw plugins enable feishu
openclaw gateway restart
openclaw status --all
```

### 添加通道（以交互方式）
```bash
openclaw channels add
```

### 技能（workspace 技能）
- 目录：`workspace/skills/<skill-name>/SKILL.md`
- 已有：`notion`、`prompt-engineering-expert`、`personal-productivity`

## 3.2 基础配置建议

1. **先白名单后启用**：生产环境建议设置 `plugins.allow` 仅允许已评审插件。  
2. **单通道灰度**：每次只启用 1 个新通道，观察 24h。  
3. **最小权限凭据**：只给必要 scope，不给全量管理权限。  
4. **分环境密钥**：测试/生产账号分离。

## 3.3 常用调用指令

```bash
openclaw status
openclaw status --all
openclaw status --deep
openclaw gateway status
openclaw gateway restart
openclaw channels list
openclaw plugins list
openclaw pairing list feishu
openclaw pairing approve feishu <CODE>
```

## 3.4 注意事项
- 禁止一次性启用大量外部通道（先灰度再放量）。
- 配对码、App Secret、Bot Token 不得写入公开仓库。
- 对外通道统一走审批策略（尤其客服/财务相关）。

---

## 4) 完整测试报告

## 4.1 运行稳定性
- `openclaw plugins list` 可稳定返回 42 个插件元信息（含状态/来源/版本）。
- 关键官方插件为 `stock:` 来源，版本集中在 `2026.3.13`，维护连续。
- 本机微信通道 `openclaw-weixin` 当前为 loaded，已在会话环境运行。

结论：**核心能力稳定，适合按白名单逐步启用。**

## 4.2 兼容性
- Windows 环境命令可执行；通道启用依赖外部平台凭据（飞书/企业微信/Slack 等）。
- 技能与插件可并行使用（如 Notion skill + Feishu channel）。

结论：**兼容性良好，主要风险在外部账号权限配置。**

## 4.3 异常行为检测
- 未发现强制弹窗、广告注入、异常后台上传行为（基于 CLI/元信息层）。
- 发现部分 npm 包名不可见或 404（详见问题清单），已从推荐中降级或替换为 stock 插件路径。

结论：**当前推荐清单未发现高风险异常行为。**

## 4.4 风险提示
1. 多通道同时启用会扩大数据面，必须做最小权限。  
2. 社区维护插件要锁版本并定期复核。  
3. 生产环境建议启用审计日志与配对审批。

## 4.5 综合推荐等级
- **S 级推荐（立即可上）：** notion、feishu、slack、memory-core、LLM Task、Lobster、matrix
- **A 级推荐（灰度后上）：** weixin、msteams、mattermost、nextcloud-talk、signal、voice-call
- **暂缓：** 未收录/404/来源不清晰项

---

## 5) 落地执行清单（建议你下个工作日直接用）

1. 先固定 `plugins.allow` 白名单（S级优先）。  
2. 第一批启用：`feishu + notion + memory-core`。  
3. 第二批启用：`weixin + whatsapp/telegram`（视业务范围）。  
4. 每批次观察 24h：错误率、消息延迟、权限告警。  
5. 周期复检：每周一次 `plugins list + status --deep`。

---

> 本文档用于公司插件/技能采购与启用决策，不构成最终安全审计替代。生产落地前建议由运维/安全负责人做二次审批。
