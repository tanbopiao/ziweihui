"""巡（XUN）· 巡衡官：审计留痕，讳不落地。

命名即种子：用必受巡衡审计——谁在何时赐讳、验讳、拒讳，全量可查；
台账只记讳的哈希指纹，讳值本身永不落明文。
"""


class Xun:
    """巡衡官：全量审计台账（只记指纹，不记明文）。"""

    CODE = "XUN"

    def __init__(self):
        self._ledger = []

    def record(self, action, fingerprint, actor=None):
        """记一笔：grant / verify_pass / verify_reject。"""
        import time

        entry = {
            "action": action,
            "fingerprint": fingerprint,
            "actor": actor,
            "ts": time.strftime("%Y-%m-%dT%H:%M:%S+08:00", time.localtime()),
        }
        self._ledger.append(entry)
        return entry

    def ledger(self, action=None):
        """查台账：可按动作过滤；每笔含指纹与时间，无明文讳值。"""
        if action is None:
            return list(self._ledger)
        return [e for e in self._ledger if e["action"] == action]

    def summary(self):
        """对账摘要：赐、销、拒各多少笔。"""
        return {
            "grant": len(self.ledger("grant")),
            "verify_pass": len(self.ledger("verify_pass")),
            "verify_reject": len(self.ledger("verify_reject")),
        }
