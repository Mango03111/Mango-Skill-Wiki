# code-assistance

本分类用于存放与代码贡献、开源协作、代码审查、提交规范、PR 工作流、CI 触发和工程实践相关的 Skills。

## Skills

| Skill | 说明 | 可上传压缩包 |
|---|---|---|
| [`vllm-ascend-contribution`](./vllm-ascend-contribution/) | 引导 AI Agent 完成 vllm-ascend 贡献流程，包括 DCO 签署、PR 标题与正文规范、本地检查、文档变更、多节点测试和 E2E/nightly CI 触发 | [`vllm-ascend-contribution.skill.zip`](./%23skillPackage/vllm-ascend-contribution.skill.zip) |
| [`competition-version-iteration`](./competition-version-iteration/) | 安全维护 Git 项目版本历史，包括初始化发布分支配置、提交并标记新版本，以及在不更改标签的前提下记录赛后结果 | [`competition-version-iteration.skill.zip`](./%23skillPackage/competition-version-iteration.skill.zip) |

## 使用方式

1. 进入 [`#skillPackage`](./%23skillPackage/) 文件夹；
2. 下载对应的 `.skill.zip` 压缩包；
3. 在支持 Skills 的 ChatGPT 环境中上传并安装；
4. 打开或上传相关 Git 项目、代码变更、PR 信息、CI 日志或文档资料；
5. 使用类似下面的提示词调用：

```text
使用 vllm-ascend-contribution 技能，帮我准备符合 vllm-ascend 规范的提交和 PR。
```

```text
使用 competition-version-iteration 技能，帮我安全发布或记录这个项目的版本。
```
