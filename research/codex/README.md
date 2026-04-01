# Codex 资料总入口

> 用途：作为 GitHub / Notion 的统一导读页，串联当前这套 Codex 中文资料，避免入口分散与版本漂移。

## 资料结构

### 01. 团队导读
- [`codex-team-readme.md`](./codex-team-readme.md)
- 用途：给管理者、工程负责人、试点成员快速建立统一认知
- 特点：短、轻、可转发、低门槛

### 02. 使用指南
- [`codex-guide.md`](./codex-guide.md)
- 用途：介绍入口、能力边界、skills、团队落地建议
- 适合：需要系统了解 Codex 的同学

### 03. 提示词模板
- [`codex-prompt-templates.md`](./codex-prompt-templates.md)
- 用途：直接复用的 prompt 模板库
- 适合：执行者、任务定义者、review 协作者

### 04. 内部培训包 / SOP
- [`codex-training-sop.md`](./codex-training-sop.md)
- 用途：团队试点、执行、review、验收、沉淀的内部规范
- 适合：团队实施者、质量角色、培训组织者

### 05. 研究来源清单
- [`sources.md`](./sources.md)
- 用途：回溯来源、核对事实边界、发布前复核
- 适合：审稿、复核、二次发布

## 推荐阅读顺序

### 如果你是第一次接触
1. 团队导读
2. 使用指南
3. 内部培训包 / SOP
4. 提示词模板
5. 来源清单

### 如果你要直接落地试点
1. 团队导读
2. 提示词模板
3. 内部培训包 / SOP
4. 使用指南
5. 来源清单

### 如果你要做审稿 / 发布
1. 总入口
2. 使用指南
3. 内部培训包 / SOP
4. 来源清单

## 文档关系说明

- 导读页负责“低门槛入口”，不替代指南或培训稿
- 使用指南负责“能力与边界说明”，不替代 SOP
- SOP 负责“内部采用与执行规范”，不扩写成知识总览
- 来源清单负责“证据与映射”，不承担培训功能

## 发布前最小校验

- [ ] GitHub / Notion 标题与顺序一致
- [ ] 总入口能跳到 guide / prompt templates / training SOP / sources
- [ ] SOP 能回链到 guide / prompt templates / sources
- [ ] 不出现断链、重复、版本漂移
