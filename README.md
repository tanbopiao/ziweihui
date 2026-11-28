# ziweihui · 紫薇讳

**同一体系的两层构件：根级特权令（PRV-01）＋ 元枢算子层。**

> 命名即种子：紫薇讳＝帝座亲赐之讳，「讳出宸极，莫见其全」。名字所对应的逻辑与架构，是从种子长出来的。
> 正字为「紫薇」（2026-11-28 宗源裁示）；早期记录中的「紫微讳」为历史原称，保留不改。

## 架构层级

| 层级 | 职责 | 入口 |
|------|------|------|
| 根级特权令 | 全体系唯一越权口：帝座独赐、一讳一用、讳不落地 | `ziweihui.Ziweihui`（赐/验/巡三官） |
| 元枢算子层 | 唯一可执行单元（符）：签名、逻辑体、依赖、边界四位一体 | `yuanshu`（首批四算子） |

## 命名映射（道统 → 架构）

### 根级特权令（赐 · 验 · 巡）

| 道 | 义 | 算子 |
|----|----|------|
| 赐 | 帝座独赐，一讳一用，发一次性根级特权令 | `Ci` 赐讳官 |
| 验 | 验讳即销，一讳只能用一次，二次用即拒并留痕 | `Yan` 验讳官 |
| 巡 | 赐讳、验讳、拒讳全量可查，讳值不落明文台账（只记哈希指纹） | `Xun` 巡衡官 |

逻辑本体：**越权口必须唯一、一次性、可审计——三权分立，讳值本身永不落明文。**
不是提醒审计员别记明文，而是结构上台账里就只有指纹。

### 元枢算子层（首批四算子，低风险查询/校验类）

| 算子 | 职责 | 副作用边界 |
|------|------|-----------|
| `yuanshu.digest` | 会话摘要：结论 + 要点，硬筛门过滤疑似密钥行 | 仅归一层回归 |
| `yuanshu.search` | 记忆检索：查询词含密钥片段直接拒查，命中敏感行不进结果 | 无（纯只读） |
| `yuanshu.snapshot` | 台账快照：总数、分类计数、最新条目 | 无（纯只读） |
| `yuanshu.lint` | 语义规格校验：七项必备条目齐全性 | 无（纯只读） |

每件算子配套语义规格（`docs/spec/`）与算子契约（`docs/dsl/`）：
签名（符头）、逻辑体（符身）、依赖（符胆）、边界（符脚）四位一体。

## 安装

零第三方依赖，仅 Python 3.10+ 标准库。

```bash
git clone https://github.com/tanbopiao/ziweihui.git
cd ziweihui
python -m unittest discover -s tests -v   # 自测
python examples/demo_privilege.py         # 特权令端到端演示
```

## 用法

### 根级特权令

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

### 元枢算子层

```python
from yuanshu import digest, search, snapshot, lint

# 会话摘要（敏感行自动过滤）
print(digest({"session_id": "s1", "content": "结论先行\n要点甲\napi_key = sk-xxxx"}))

# 记忆检索（查询词带密钥片段会被拒查）
print(search({"query": "加固", "corpus": {"a1": "第一批三道加固"}}))

# 台账快照
print(snapshot({"entries": [{"type": "deploy", "timestamp": "2026-11-28"}]}))

# 语义规格校验
print(lint({"spec_text": open("docs/spec/ops.spec.lint.spec.md", encoding="utf-8").read()}))
```

## 自测

```bash
python -m unittest discover -s tests -v
```

## 许可

MIT
