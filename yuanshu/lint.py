# ops.spec.lint v0.1.0（模板模式实现）
# 契约：dsl/ops.spec.lint.dsl.yaml；规格：spec/ops.spec.lint.spec.md
# 纯只读校验：语义规格必备条目齐全性检查。

VERSION = "0.1.0"
ALLOWED_SIDE_EFFECTS = []
REQUIRED_SECTIONS = ["算子名", "输入", "输出", "前置条件", "副作用边界", "风险级别", "筛门"]


def run(inputs: dict) -> dict:
    spec_text = inputs.get("spec_text")
    if not spec_text or not isinstance(spec_text, str):
        return {"ok": False, "error": "invalid spec_text"}

    missing = [s for s in REQUIRED_SECTIONS if s not in spec_text]
    warnings = []
    if "验收口径" not in spec_text:
        warnings.append("缺「验收口径」节，建议补齐")
    if "## 条目" not in spec_text:
        warnings.append("缺「## 条目」节标题")

    return {
        "ok": len(missing) == 0,
        "missing": missing,
        "warnings": warnings,
        "operator": f"ops.spec.lint@{VERSION}",
    }
