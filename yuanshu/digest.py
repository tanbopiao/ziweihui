# ops.memory.digest v0.2.0（模板模式增强实现）
# 契约：dsl/ops.memory.digest.dsl.yaml；规格：spec/ops.memory.digest.spec.md
# v0.2.0 变更：结论行同样过硬筛门；要点去重；单行长度截断；空摘要保护。
# 接模型后由「模型补实现」替换 _summarize 内核，契约与边界不变。

VERSION = "0.2.0"
ALLOWED_SIDE_EFFECTS = ["hub.archive.append"]
MAX_LINE = 120
MAX_POINTS = 5


def run(inputs: dict) -> dict:
    session_id = inputs.get("session_id")
    if not session_id or not isinstance(session_id, str):
        return {"ok": False, "error": "invalid session_id"}

    content = inputs.get("content")
    if not content or not isinstance(content, str):
        return {"ok": False, "error": "session not found or empty"}

    digest = _summarize(content)
    return {
        "ok": True,
        "digest": digest,
        "operator": f"ops.memory.digest@{VERSION}",
    }


def _summarize(content: str) -> str:
    """抽取式摘要：首条非敏感行为结论，其后取要点行（去重、截断，至多 5 行）。
    硬筛门：疑似密钥/敏感字段行不入摘要（含结论行）。"""
    lines = [ln.strip() for ln in content.splitlines() if ln.strip()]
    safe = [ln for ln in lines if not _suspicious(ln)]
    if not safe:
        return "（空会话）"
    conclusion = safe[0][:MAX_LINE]
    seen, points = {conclusion}, []
    for ln in safe[1:]:
        key = ln[:MAX_LINE]
        if key not in seen:
            seen.add(key)
            points.append(key)
        if len(points) >= MAX_POINTS:
            break
    out = f"结论：{conclusion}"
    if points:
        out += "\n" + "\n".join(f"- {p}" for p in points)
    return out


def _suspicious(line: str) -> bool:
    """硬筛门：疑似密钥/敏感字段行不入摘要。"""
    lowered = line.lower()
    markers = ("key", "token", "secret", "password", "bearer ", "sk-", "passwd", "credential")
    return any(m in lowered for m in markers)
