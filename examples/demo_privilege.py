"""紫微讳端到端演示：赐→验→再验（拒）→巡审计。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ziweihui import Ziweihui

gate = Ziweihui()

# 赐：帝座独赐一讳
token = gate.grant(issuer="帝座")
print("赐讳：一枚 32 位讳值已独赐（此处不展示明文）")

# 验：首次验讳，放行即焚
print("首次验讳：", gate.verify(token, actor="守卫"))

# 再验：一讳一用，二次即拒
print("二次验讳：", gate.verify(token, actor="守卫"))

# 巡：审计台账全量可查，讳不落地（只记指纹）
for entry in gate.audit():
    print(entry)
print("对账摘要：", gate.audit_summary())
