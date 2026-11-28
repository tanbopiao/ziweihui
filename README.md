# ziweihui · 紫微讳

**PRV-01 根级特权令：帝座独赐、一讳一用、讳不落地。**

> 命名即种子：紫微讳＝全体系唯一越权口，「讳出宸极，莫见其全」。名字所对应的逻辑与架构，是从种子长出来的。

## 命名映射（道统 → 架构）

| 道 | 义 | 算子 |
|----|----|------|
| 赐 | 帝座独赐，一讳一用，发一次性根级特权令 | `Ci` 赐讳官 |
| 验 | 验讳即销，一讳只能用一次，二次用即拒并留痕 | `Yan` 验讳官 |
| 巡 | 赐讳、验讳、拒讳全量可查，讳值不落明文台账（只记哈希指纹） | `Xun` 巡衡官 |

逻辑本体：**越权口必须唯一、一次性、可审计——三权分立，讳值本身永不落明文。**
不是提醒审计员别记明文，而是结构上台账里就只有指纹。

## 安装

零第三方依赖，仅 Python 3.10+ 标准库。

```bash
git clone https://github.com/tanbopiao/ziweihui.git
cd ziweihui
python -m unittest discover -s tests -v   # 自测
python examples/demo_privilege.py         # 端到端演示
```

## 用法

```python
from ziweihui import Ziweihui

gate = Ziweihui()

# 赐：帝座独赐一讳
token = gate.grant(issuer="帝座")

# 验：验讳即销，通过放行
print(gate.verify(token, actor="守卫"))    # {'granted': True, 'one_time': True, ...}

# 再验：一讳一用，二次即拒
print(gate.verify(token, actor="守卫"))    # {'granted': False, 'reason': '未赐或已焚', ...}

# 巡：审计台账全量可查，只含指纹
print(gate.audit_summary())               # {'grant': 1, 'verify_pass': 1, 'verify_reject': 1}
```

原单文件骨架 API（`describe()` / `grant()` / `use()`）收编保留，行为不变。

## 自测

```bash
python -m unittest discover -s tests -v
```

## 许可

MIT
