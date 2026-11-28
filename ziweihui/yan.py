"""验（YAN）· 验讳官：验讳即销，一讳只能用一次。

命名即种子：临文不讳——验讳官只认讳值与已焚账：在册未焚则放行并当场核销，
已焚、未赐或伪造之讳一律拒斥；本官只记讳的哈希指纹，明文讳值不留底。
"""

import hashlib


class Yan:
    """验讳官：用即核销，重复即拒，只记指纹。"""

    CODE = "YAN"

    def __init__(self, burn=None):
        # burn：核销回调（门面注入 legacy.use，一讳一用语义同源）；
        # 独立使用时无发行方，验讳官自行按「真讳形制」把关。
        self._burn = burn
        self._burned = set()
        self.events = []

    @staticmethod
    def fingerprint(token):
        return hashlib.sha256(token.encode()).hexdigest()[:16]

    @staticmethod
    def _well_formed(token):
        """真讳形制：32 位十六进制串（与铸讳形制同源），伪造之讳形制即露馅。"""
        return isinstance(token, str) and len(token) == 32 and all(c in "0123456789abcdef" for c in token)

    def verify(self, token, actor=None):
        """验讳：放行即核销；伪造、未赐或已焚即拒。只返回指纹，不回明文。"""
        fp = self.fingerprint(token)
        if fp in self._burned:
            self.events.append({"event": "reject", "reason": "burned", "fingerprint": fp})
            return {"granted": False, "reason": "讳不可用：一讳一用，此讳已焚", "fingerprint": fp}
        if self._burn is not None:
            try:
                self._burn(token)
            except PermissionError:
                self.events.append({"event": "reject", "reason": "not_granted", "fingerprint": fp})
                return {"granted": False, "reason": "讳不可用：未赐或已焚", "fingerprint": fp}
        else:
            if not self._well_formed(token):
                self.events.append({"event": "reject", "reason": "forged", "fingerprint": fp})
                return {"granted": False, "reason": "讳不可用：伪造之讳", "fingerprint": fp}
        self._burned.add(fp)
        self.events.append({"event": "consume", "fingerprint": fp})
        return {"granted": True, "one_time": True, "fingerprint": fp}

    def describe(self):
        return {"code": self.CODE, "cn": "验讳官", "duty": "验讳即销，一讳只能用一次"}
