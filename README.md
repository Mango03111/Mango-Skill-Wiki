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
| 代码辅助 | [`code-assistance`](./code-assistance/) | 用于开源贡献、代码审查、提交规范、PR 工作流、CI 触发和工程协作等场景 |
| 科研阅读 | [`research`](./research/) | 用于学术论文阅读、研究工作流、结构化笔记、真实问答记录和 Skill 知识库维护等场景 |

## 已收录 Skill

### mechanical-modeling-doc

位置：[`structural-design/mechanical-modeling-doc`](./structural-design/mechanical-modeling-doc/)

该 Skill 用于根据机械设计说明书、CAD 图纸、图片、工程截图、PDF、DOCX 等资料，整理生成结构化的 SolidWorks / CAD 建模说明书。它可以输出建模概述、建模可行性分析、尺寸冲突与装配干涉检查、零件清单、零件尺寸规格、功能位置、装配配合关系、运动仿真设置和完整 Markdown 建模文档。

### vllm-ascend-contribution

位置：[`code-assistance/vllm-ascend-contribution`](./code-assistance/vllm-ascend-contribution/)

该 Skill 用于引导 AI Agent 完成 `vllm-project/vllm-ascend` 仓库的贡献流程。它覆盖变更范围判断、本地 lint/CI/测试选择、DCO `Signed-off-by` 提交、PR 标题与正文规范、文档变更、多节点测试配置，以及 E2E/nightly 硬件 CI 触发评论等流程。

### competition-version-iteration

位置：[`code-assistance/competition-version-iteration`](./code-assistance/competition-version-iteration/)

该 Skill 用于安全维护竞赛或其他 Git 项目的版本历史。它可以初始化正式发布分支配置，在用户明确授权后发布带提交和注释标签的新版本，或将用户提供的赛后结果追加到版本记录中，同时避免改写已发布标签和历史。

### read-paper-with-notes

位置：[`research/read-paper-with-notes`](./research/read-paper-with-notes/)

该 Skill 用于陪伴式、分章节阅读学术论文，并同步维护简洁的 Markdown 阅读笔记。它强调先读懂论文的问题、方法、证据和局限，再按章节解释重点段落、关键词、图表和机制，同时只记录用户实际提出过的问题与简要回答，适合组会、汇报或深入理解论文前的阅读准备。

### mango-skill-helper

位置：[`research/mango-skill-helper`](./research/mango-skill-helper/)

该 Skill 用于把新的 ChatGPT Skill 规范加入 Mango Skill Wiki。它会要求用户先选择现有分类文件夹或新建根目录分类文件夹，然后按仓库既有模式整理源码目录、`.skill.zip` 压缩包、分类 README，并同步补充根目录中英文 README。

## 使用方式

1. 下载对应 Skill 文件夹或 `.skill.zip` 文件；
2. 在支持 Skills 的 ChatGPT 环境中上传并安装；
3. 在聊天中上传相关项目资料；
4. 使用类似下面的提示词调用：

```text
使用 mechanical-modeling-doc 技能，帮我把这些资料整理成完整 SolidWorks 建模说明书。
```

```text
使用 vllm-ascend-contribution 技能，帮我准备符合 vllm-ascend 规范的提交和 PR。
```

```text
使用 competition-version-iteration 技能，帮我安全发布或记录这个项目的版本。
```

```text
使用 read-paper-with-notes 技能，带我按章节读懂这篇论文，并维护一份简洁的阅读笔记。
```

```text
使用 mango-skill-helper 技能，帮我把这个 skill 加入指定分类，并同步更新 README。
```

## 交流与改进

欢迎大家通过 Issue、Discussion 或 Pull Request 交流使用体验、改进建议和新的 Skill 想法。

如果某个 Skill 对你有帮助，也欢迎基于它扩展出更适合自己工作流的版本。
