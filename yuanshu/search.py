# ops.memory.search v0.1.0（模板模式实现）
# 契约：dsl/ops.memory.search.dsl.yaml；规格：spec/ops.memory.search.spec.md
# 纯只读检索：子串匹配 + 硬筛门双向（query 拒查、命中行过滤）。

VERSION = "0.1.0"
ALLOWED_SIDE_EFFECTS = []
MAX_MATCHES = 5
MAX_SNIPPET = 120
_SECRET_MARKERS = ("key", "token", "secret", "password", "bearer ", "sk-", "passwd", "credential")


def run(inputs: dict) -> dict:
    query = inputs.get("query")
    if not query or not isinstance(query, str):
        return {"ok": False, "error": "invalid query"}
    if _suspicious(query):
        return {"ok": False, "error": "query rejected by hard gate"}

    corpus = inputs.get("corpus")
    if not isinstance(corpus, dict):
        return {"ok": False, "error": "invalid corpus"}

    q = query.strip().lower()
    matches, total = [], 0
    for item_id in sorted(corpus):
        text = corpus[item_id]
        if not isinstance(text, str):
            continue
        for ln in text.splitlines():
            line = ln.strip()
            if q in line.lower():
                total += 1
                if len(matches) < MAX_MATCHES and not _suspicious(line):
                    matches.append({"id": item_id, "snippet": line[:MAX_SNIPPET]})

    return {
        "ok": True,
        "matches": matches,
        "total": total,
        "operator": f"ops.memory.search@{VERSION}",
    }


def _suspicious(line: str) -> bool:
    lowered = line.lower()
    return any(m in lowered for m in _SECRET_MARKERS)
