# Mango Skill Wiki

[English Version](./README.en.md)

## 仓库简介

本仓库用于存放和分享我在生产实践、学习研究和项目开发过程中沉淀出来的实用 ChatGPT Skills。每一个 Skill 都对应一个具体的重复性工作流，目标是把复杂、多步骤、容易遗漏细节的任务整理成可复用、可迁移、可交流的标准化能力。

我希望通过这个仓库，把自己在实际项目中验证过、觉得好用的 Skill 逐步整理出来，方便后续复用，也希望能帮助到有类似需求的朋友。欢迎大家交流、改进和提出建议。

## 仓库用途

本仓库主要用于：

- 保存本人在生产实践中产出的高频实用 Skill；
- 记录每个 Skill 的适用场景、输入资料和输出结果；
- 分享可复用的工作流、文档模板和分析规范；
- 方便他人下载、学习、修改和二次开发；
- 作为个人 Skill 知识库和案例库持续维护。

## 当前分类

| 分类 | 文件夹 | 说明 |
|---|---|---|
| 结构设计 | [`structural-design`](./structural-design/) | 用于机械结构设计、CAD/SolidWorks 建模说明书、装配分析、尺寸冲突检查等场景 |

## 已收录 Skill

### mechanical-modeling-doc

位置：[`structural-design/mechanical-modeling-doc`](./structural-design/mechanical-modeling-doc/)

该 Skill 用于根据机械设计说明书、CAD 图纸、图片、工程截图、PDF、DOCX 等资料，整理生成结构化的 SolidWorks / CAD 建模说明书。它可以输出建模概述、建模可行性分析、尺寸冲突与装配干涉检查、零件清单、零件尺寸规格、功能位置、装配配合关系、运动仿真设置和完整 Markdown 建模文档。

## 使用方式

1. 下载对应 Skill 文件夹或 `.skill.zip` 文件；
2. 在支持 Skills 的 ChatGPT 环境中上传并安装；
3. 在聊天中上传相关项目资料；
4. 使用类似下面的提示词调用：

```text
使用 mechanical-modeling-doc 技能，帮我把这些资料整理成完整 SolidWorks 建模说明书。
```

## 交流与改进

欢迎大家通过 Issue、Discussion 或 Pull Request 交流使用体验、改进建议和新的 Skill 想法。

如果某个 Skill 对你有帮助，也欢迎基于它扩展出更适合自己工作流的版本。
