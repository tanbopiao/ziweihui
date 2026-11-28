"""紫微讳（ZIWEIHUI）· 根级特权令：帝座独赐、一讳一用、讳不落地、临文不讳。

命名即种子：紫微讳＝全体系唯一越权口，「讳出宸极，莫见其全」。
逻辑本体：越权口必须唯一、一次性、可审计——赐（发讳）、验（销讳）、
巡（审计）三权分立，讳值本身永不落明文台账，只记哈希指纹。

三算子：
- 赐（ci.Ci）    赐讳官：帝座独赐，一讳一用，发一次性根级特权令。
- 验（yan.Yan）  验讳官：验讳即销，一讳只能用一次，二次用即拒并留痕。
- 巡（xun.Xun）  巡衡官：赐讳、验讳、拒讳全量可查，讳值不落明文。

三算子合枢于 Ziweihui 门面（grant / verify / audit）。
原单文件骨架 API（describe / grant / use）收编保留，行为不变。
"""

import hashlib

from .legacy import Ziweihui as _LegacyZiweihui
from .ci import Ci
from .yan import Yan
from .xun import Xun

__all__ = ["Ziweihui", "Ci", "Yan", "Xun"]


class Ziweihui(_LegacyZiweihui):
    """紫微讳门面：原 v1 API 之上长出赐/验/巡三算子。"""

    def __init__(self, config=None):
        super().__init__(config)
        self._ci = Ci()
        self._yan = Yan(burn=self.use)  # 销讳委托给 legacy.use，一讳一用语义同源
        self._xun = Xun()

    def grant(self, issuer="帝座"):
        """赐：独赐一讳。原 v1 行为不变（返回讳值并登记可焚），另记审计。"""
        token = super().grant()
        fingerprint = hashlib.sha256(token.encode()).hexdigest()[:16]
        self._ci.issue(issuer=issuer)
        self._xun.record("grant", fingerprint, actor=issuer)
        return token

    def verify(self, token, actor=None):
        """验：验讳即销；通过放行，未赐或已焚即拒，全部留痕。"""
        fingerprint = hashlib.sha256(token.encode()).hexdigest()[:16]
        result = self._yan.verify(token, actor=actor)
        self._xun.record("verify_pass" if result["granted"] else "verify_reject",
                         fingerprint, actor=actor)
        return result

    def audit(self, action=None):
        """巡：审计台账全量可查（只含指纹，不含明文讳值）。"""
        return self._xun.ledger(action)

    def audit_summary(self):
        """巡：赐、销、拒对账摘要。"""
        return self._xun.summary()
