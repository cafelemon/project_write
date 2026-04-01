# Codex 研究来源清单与正文映射（发布版）

> 说明：本清单优先保留官方来源，并补充“正文对应章节”映射，便于发布后追溯。  
> 使用原则：**官方来源优先；仓库目录类信息视为当前快照；变化快的产品细节应标注为待复核。**

## 一、正文章节与来源映射索引

| 正文章节 | 主要支撑来源 | 备注 |
|---|---|---|
| 1. Codex 是什么 | OpenAI 官方发布；`openai/codex` README | 用于界定 Codex 的产品族与代理能力 |
| 2. Quick Start | `openai/codex` README；官方发布 | 以官方入口为基础，加入实践建议 |
| 3. CLI / Web / IDE / App 入口 | 官方发布；`openai/codex` README；开发者文档入口 | 其中 IDE / App 细节仍建议发布前复核 |
| 4. GitHub review / MCP / Web search / skills | OpenAI 升级说明；`openai/skills` README | 对变化快的能力单列待复核 |
| 5. skills 代表性样例 | `openai/skills` README；样例 `SKILL.md`；GitHub 目录快照 | 明确不是稳定完整目录 |
| 6. AGENTS.md / rules / skills 分工 | 官方发布；`openai/skills` README | 其中“rules”更多是实践归纳表达 |
| 7. 推荐工作流 | 官方材料 + 实践归纳 | 属方法论，不应误写成官方硬性规则 |
| 8. 推荐 skills / 工具清单 | 官方样例 + 团队落地经验 | 明确为推荐，不是官方套餐 |
| 9. 团队落地建议 | 实践归纳 | 需与“官方已明确”严格区分 |
| 10. 待正式发布前复核 | 官方入口页、升级稿、仓库当前状态 | 用于控制事实边界 |

---

## 二、官方来源（最高优先级）

### A. OpenAI 官方发布与说明

1. **Introducing Codex | OpenAI**  
   https://openai.com/index/introducing-codex/  
   - 用途：确认云端代理、隔离环境、并行任务、日志与任务留痕等核心定位
   - 对应正文：第 1、2、3（Web / Cloud）、7 节

2. **Introducing upgrades to Codex | OpenAI**  
   https://openai.com/index/introducing-upgrades-to-codex/  
   - 用途：确认 GitHub review、IDE、Web search、MCP 等升级方向
   - 对应正文：第 3（IDE）、4、10 节

3. **Introducing the Codex app | OpenAI**  
   https://openai.com/index/introducing-the-codex-app/  
   - 用途：确认 App 作为桌面入口、多代理/长期任务管理的官方叙述
   - 对应正文：第 3（App）、10 节

### B. OpenAI 官方 GitHub 仓库

4. **openai/codex**  
   https://github.com/openai/codex  
   - 用途：确认 CLI 的官方开源仓库身份
   - 对应正文：第 1、2、3（CLI）节

5. **openai/codex README**  
   https://github.com/openai/codex/blob/main/README.md  
   - 用途：确认安装方式、CLI 定位、基本入口信息
   - 对应正文：第 2、3（CLI）节

6. **openai/codex docs/install.md**  
   https://github.com/openai/codex/blob/main/docs/install.md  
   - 用途：补充安装、系统要求与调试相关信息
   - 对应正文：第 3（CLI）节

### C. OpenAI 官方 Skills 仓库

7. **openai/skills**  
   https://github.com/openai/skills  
   - 用途：确认 skills 官方仓库入口
   - 对应正文：第 4、5、8 节

8. **openai/skills README**  
   https://github.com/openai/skills/blob/main/README.md  
   - 用途：确认 skills 的总体定义、安装方式、分层描述
   - 对应正文：第 4、5、6 节

9. **system / skill-installer / SKILL.md**  
   https://github.com/openai/skills/blob/main/skills/.system/skill-installer/SKILL.md  
   - 用途：确认安装器相关说明
   - 对应正文：第 4、5 节

10. **system / skill-creator / SKILL.md**  
    https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md  
    - 用途：确认 skill 目录结构、最佳实践表达
    - 对应正文：第 4、5 节

11. **curated / playwright / SKILL.md**  
    https://github.com/openai/skills/blob/main/skills/.curated/playwright/SKILL.md  
    - 用途：浏览器自动化样例
    - 对应正文：第 5、8 节

12. **curated / figma-implement-design / SKILL.md**  
    https://github.com/openai/skills/blob/main/skills/.curated/figma-implement-design/SKILL.md  
    - 用途：设计稿转前端样例
    - 对应正文：第 5、8 节

13. **curated / gh-address-comments / SKILL.md**  
    https://github.com/openai/skills/blob/main/skills/.curated/gh-address-comments/SKILL.md  
    - 用途：PR 评论处理样例
    - 对应正文：第 5、8 节

14. **curated / vercel-deploy / SKILL.md**  
    https://github.com/openai/skills/blob/main/skills/.curated/vercel-deploy/SKILL.md  
    - 用途：部署类样例
    - 对应正文：第 5、8 节

### D. OpenAI 开发者文档入口（建议正式发布前人工复核）

15. **Codex | OpenAI Developers**  
    https://developers.openai.com/codex  
    - 用途：Codex 官方文档总入口
    - 对应正文：第 3、4、10 节

16. **CLI | Codex | OpenAI Developers**  
    https://developers.openai.com/codex/cli  
    - 用途：CLI 入口页
    - 对应正文：第 3（CLI）、10 节

17. **IDE | Codex | OpenAI Developers**  
    https://developers.openai.com/codex/ide  
    - 用途：IDE 入口页
    - 对应正文：第 3（IDE）、10 节

18. **Security | Codex | OpenAI Developers**  
    https://developers.openai.com/codex/security  
    - 用途：安全与权限边界相关入口
    - 对应正文：第 4、10 节

19. **App | Codex | OpenAI Developers**  
    https://developers.openai.com/codex/app  
    - 用途：App 入口页
    - 对应正文：第 3（App）、10 节

20. **Skills | Codex | OpenAI Developers**  
    https://developers.openai.com/codex/skills  
    - 用途：skills 官方说明入口
    - 对应正文：第 4、5、10 节

21. **Create custom skills | Codex | OpenAI Developers**  
    https://developers.openai.com/codex/skills/create-skill  
    - 用途：自定义 skill 入口页
    - 对应正文：第 4、5、8、10 节

---

## 三、高可信补充来源

### GitHub 仓库目录与当前样例快照

本轮整理中，曾结合 `openai/skills` 仓库当前目录与样例 `SKILL.md` 做辅助判断，用来说明：
- 当前可见的代表性样例有哪些
- 哪些样例适合被当作“理解体系的样本”

**注意：**
这类信息反映的是“仓库当前状态”，不应被写成长期稳定目录。

---

## 四、本轮写作原则说明

### 1. 哪些内容可直接作为正文事实

可直接作为正文事实的，原则上限于：
- OpenAI 官方站点已明确表达的能力或产品定位
- OpenAI 官方 GitHub README 已明确写出的安装或结构说明
- 官方 skills 仓库中清楚写出的 skill 定义与结构

### 2. 哪些内容只适合作为实践建议

以下更适合写成经验建议，而不是官方结论：
- 入口选型建议
- 团队落地顺序
- 哪些任务先 skill 化更合适
- 哪类工作流更稳

### 3. 哪些内容必须标待复核

以下变化较快，正式发布前应再核验一次：
- ChatGPT 计划差异与权益
- IDE / App 的支持平台与安装说明
- GitHub review 的具体触发方式
- Web search、MCP 在不同入口的可用性差异
- `openai/skills` 仓库当前分类和样例列表

---

## 五、正式发布前建议补核项

1. ChatGPT 各计划当前包含的 Codex 权益与额度  
2. IDE 扩展当前支持的编辑器、版本、安装页  
3. Codex App 当前下载入口与平台支持矩阵  
4. Web search、MCP、图像输入在不同入口上的差异  
5. GitHub review 的接入条件、触发方式与帮助文档  
6. `openai/skills` 仓库当前 experimental 内容是否已公开变化  

---

## 六、引用时的可信度分级建议

- **一级（可直接引用）**：OpenAI 官方站点、OpenAI 官方 GitHub 仓库、官方 README、官方 skills 仓库  
- **二级（可辅助说明）**：GitHub 当前目录结构、样例 `SKILL.md`、官方开发者文档入口页  
- **三级（需谨慎补充）**：第三方博客、社区帖子、论坛讨论  
