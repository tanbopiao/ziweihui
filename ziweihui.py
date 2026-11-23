"""紫微讳（ZIWEIHUI）· 根级特权令：帝座独赐、一讳一用、讳不落地、临文不讳，全体系唯一越权口，用必受巡衡审计

道统出处：元极恒一·术语缩影表 T026；总铭「讳出宸极，莫见其全」 ｜ 第六批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：根级特权令：帝座独赐、一讳一用、讳不落地、临文不讳，全体系唯一越权口，用必受巡衡审计。

边界：本件为算子骨架 v0——接口先立、实现随进化轮补齐；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Ziweihui:
    """紫微讳（ZIWEIHUI）算子骨架 v0。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "ZIWEIHUI"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕

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
        """帝座独赐：签发一讳一用特权令（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("ZIWEIHUI.grant 骨架桩，候进化轮补齐")

    def use(self, token):
        """讳不落地：用即焚，用必留审计痕（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("ZIWEIHUI.use 骨架桩，候进化轮补齐")
