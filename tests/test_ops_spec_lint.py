# ops.spec.lint 沙箱用例
# 运行：python3 tests/test_ops_spec_lint.py 或 python -m unittest discover -s tests -v

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from yuanshu import lint


class TestLintOps(unittest.TestCase):
    def test_complete_spec_ok(self):
        good = open(os.path.join(os.path.dirname(__file__), '..', 'docs', 'spec', 'ops.spec.lint.spec.md'), encoding='utf-8').read(); r = lint({'spec_text': good}); self.assertTrue(r['ok']); self.assertEqual(r['missing'], [])

    def test_missing_sections_listed(self):
        r = lint({'spec_text': '# 规格\n- **算子名**：x\n- **输入**：y'}); self.assertFalse(r['ok']); self.assertIn('输出', r['missing']); self.assertIn('筛门', r['missing'])

    def test_empty_spec_full_missing(self):
        r = lint({'spec_text': '# 空'}); self.assertFalse(r['ok']); self.assertEqual(len(r['missing']), 7)

    def test_invalid_input_errors(self):
        r = lint({}); self.assertFalse(r['ok'])

    def test_version_traceable(self):
        good = open(os.path.join(os.path.dirname(__file__), '..', 'docs', 'spec', 'ops.spec.lint.spec.md'), encoding='utf-8').read(); r = lint({'spec_text': good}); self.assertIn('ops.spec.lint@', r['operator'])



if __name__ == "__main__":
    unittest.main()
