"""紫薇讳 · 元枢算子层（Yuanshu Operators）。

与根级特权令（ziweihui 门面）同属一个体系，架构层级不同：
特权令管越权口（赐/验/巡），算子层管可执行单元（符）。
四件首批算子均为低风险查询/校验类，纯只读或仅回归归一层：
- digest   会话摘要（硬筛门过滤敏感行）
- search   记忆检索（query 拒查 + 命中行过滤）
- snapshot 台账快照（总数/分类计数/最新条目）
- lint     语义规格校验（必备条目齐全性）

契约见 docs/dsl/，规格见 docs/spec/。零第三方依赖，Python 3.10+。
"""

from .digest import run as digest
from .search import run as search
from .snapshot import run as snapshot
from .lint import run as lint

__all__ = ["digest", "search", "snapshot", "lint"]
