"""赐（CI）· 赐讳官：帝座独赐，一讳一用。

命名即种子：紫微讳＝帝座独赐的根级特权令，「讳出宸极，莫见其全」。
赐讳官只管发讳：每次独赐一讳，讳值只交到受赐者手上，不落任何明文台账。
"""


class Ci:
    """赐讳官：发一次性根级特权令。"""

    CODE = "CI"

    def __init__(self):
        self._issued = []  # 会话内发讳计数留痕（不含讳值）

    def issue(self, issuer="帝座"):
        """独赐一讳：返回讳值本身；台账只记一枚指纹。"""
        import hashlib
        import time

        token = hashlib.sha256(str(time.time_ns()).encode()).hexdigest()[:32]
        fingerprint = hashlib.sha256(token.encode()).hexdigest()[:16]
        self._issued.append({"fingerprint": fingerprint, "issuer": issuer})
        return token

    @property
    def issued_count(self):
        return len(self._issued)

    def issued_fingerprints(self):
        """已赐讳的指纹清单（讳值永不在此）。"""
        return [r["fingerprint"] for r in self._issued]
