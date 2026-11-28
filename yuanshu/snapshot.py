# ops.ledger.snapshot v0.1.0（模板模式实现）
# 契约：dsl/ops.ledger.snapshot.dsl.yaml；规格：spec/ops.ledger.snapshot.spec.md
# 纯只读统计：总数、按类型计数、最新一条；缺 type 计入「未分类」。

VERSION = "0.1.0"
ALLOWED_SIDE_EFFECTS = []
UNCLASSIFIED = "未分类"


def run(inputs: dict) -> dict:
    entries = inputs.get("entries")
    if not isinstance(entries, list):
        return {"ok": False, "error": "invalid entries"}

    by_type, latest = {}, None
    for e in entries:
        if not isinstance(e, dict):
            continue
        etype = e.get("type") or UNCLASSIFIED
        by_type[etype] = by_type.get(etype, 0) + 1
        ts = e.get("timestamp") or ""
        if latest is None or ts > latest["timestamp"]:
            latest = {"type": etype, "timestamp": ts}

    return {
        "ok": True,
        "snapshot": {
            "total": len(entries),
            "by_type": by_type,
            "latest": latest,
        },
        "operator": f"ops.ledger.snapshot@{VERSION}",
    }
