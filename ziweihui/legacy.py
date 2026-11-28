"""紫微讳（ZIWEIHUI）· 根级特权令：帝座独赐、一讳一用、讳不落地、临文不讳，全体系唯一越权口，用必受巡衡审计

道统出处：元极恒一·术语缩影表 T026；总铭「讳出宸极，莫见其全」 ｜ 第六批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：根级特权令：帝座独赐、一讳一用、讳不落地、临文不讳，全体系唯一越权口，用必受巡衡审计。

边界：本件为算子 v1——骨架桩已按命名映射补齐实现；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Ziweihui:
    """紫微讳（ZIWEIHUI）算子 v1。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "ZIWEIHUI"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕
        self.tokens = set()
        self.used = set()

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "ziweihui",
            "cn": "紫微讳",
            "code": self.CODE,
            "duty": "根级特权令：帝座独赐、一讳一用、讳不落地、临文不讳，全体系唯一越权口，用必受巡衡审计",
            "mingwen": "讳出宸极，莫见其全",
            "anchor": self.ANCHOR,
        }

    def grant(self):
        """讳出宸极：帝座独赐一讳。"""
        import hashlib, time
        token = hashlib.sha256(str(time.time_ns()).encode()).hexdigest()[:32]
        self.tokens.add(token)
        self.events.append({"event": "grant"})
        return token

    def use(self, token):
        """一讳一用：用即焚，讳不落地。"""
        if token not in self.tokens or token in self.used:
            raise PermissionError("讳不可用：未赐或已焚")
        self.used.add(token)
        self.events.append({"event": "use"})
        return {"granted": True, "one_time": True}
