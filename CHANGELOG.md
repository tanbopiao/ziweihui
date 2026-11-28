# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/), and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.2.0] - 2026-11-28

### Added
- `yuanshu` 元枢算子层：首批四算子（低风险查询/校验类）
  - `digest` 会话摘要（硬筛门过滤疑似密钥行）
  - `search` 记忆检索（query 拒查 + 命中行过滤）
  - `snapshot` 台账快照（总数/分类计数/最新条目）
  - `lint` 语义规格校验（必备条目齐全性）
- 每件算子配套语义规格（`docs/spec/`）与算子契约（`docs/dsl/`）
- `CONTRIBUTING.md` 与本变更记录

### Changed
- 正字更正：「紫薇讳」为正确写法（2026-11-28 裁示）；「紫微讳」为历史原称，早期记录保留不改

## [0.1.0] - 2026-11-23

### Added
- PRV-01 根级特权令：赐（Ci）/ 验（Yan）/ 巡（Xun）三官分立
- 原单文件骨架 API（describe / grant / use）收编保留
