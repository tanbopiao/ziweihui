# 语义规格 · ops.ledger.snapshot

> 七步流水线第 1 步：需求入账。挂语义层概念「台账快照」。

## 条目

- **算子名**：ops.ledger.snapshot
- **输入**：entries（list[dict]）——台账条目（模板模式注入，接中枢后经 hub.ledger.read）；每条含 type（string）与 timestamp（string，绝对日期）
- **输出**：snapshot（dict）——{total, by_type, latest}：总数、按类型计数、最新一条的 type+timestamp
- **前置条件**：entries 可读且为列表
- **副作用边界**：无（纯只读）；禁止网络、禁止文件系统直写
- **风险级别**：低（查询只读类，设计稿灰度首选）
- **筛门**：hard + soft

## 验收口径

- 空台账 → ok=true 且 total=0，不报错。
- 条目缺 type → 计入「未分类」，不丢弃。
- timestamp 取字典序最大者为最新（绝对日期格式保证可比）。
- 产出必带算子版本号，可回溯。
