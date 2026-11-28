# 语义规格 · ops.spec.lint

> 七步流水线第 1 步：需求入账。挂语义层概念「规格校验」。

## 条目

- **算子名**：ops.spec.lint
- **输入**：spec_text（string）——语义规格全文（markdown）
- **输出**：missing（list）——缺失的必备条目名；warnings（list）——结构提示；ok（bool）——必备条目齐全
- **前置条件**：spec_text 非空
- **副作用边界**：无（纯只读）；禁止网络、禁止文件系统直写
- **风险级别**：低（本地校验类）
- **筛门**：hard + soft

## 验收口径

- 必备条目：算子名、输入、输出、前置条件、副作用边界、风险级别、筛门——缺任一列入 missing 且 ok=false。
- 空规格 → ok=false 且 missing 为全量。
- 产出必带算子版本号，可回溯。
