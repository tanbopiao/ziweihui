# 语义规格 · ops.memory.search

> 七步流水线第 1 步：需求入账。挂语义层概念「记忆检索」。

## 条目

- **算子名**：ops.memory.search
- **输入**：query（string）——检索词；corpus（dict[id, text]）——待检索语料（模板模式注入，接中枢后经 hub.ledger.read）
- **输出**：matches（list）——命中条目 {id, snippet}，至多 5 条；total（int）——命中总数
- **前置条件**：corpus 可读；query 非空
- **副作用边界**：无（纯只读）；禁止网络、禁止文件系统直写
- **风险级别**：低（查询只读类，设计稿灰度首选）
- **筛门**：hard + soft

## 验收口径

- query 含疑似密钥片段 → 直接拒绝执行（硬筛门，不回显）。
- 命中行含疑似密钥/敏感字段 → 该行不入结果。
- 空语料/无命中 → ok=true 且 matches 为空，不报错。
- 产出必带算子版本号，可回溯。
