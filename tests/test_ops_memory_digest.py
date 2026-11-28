# ops.memory.digest 沙箱用例
# 运行：python3 tests/test_ops_memory_digest.py 或 python -m unittest discover -s tests -v

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from yuanshu import digest


class TestDigestOps(unittest.TestCase):
    def test_normal_digest(self):
        r = digest({'session_id': 's1', 'content': '今晚定了分身方案\n第一批三道加固\n12月1号开工\n写类候令'}); self.assertTrue(r['ok']); self.assertTrue(r['digest'].startswith('结论：今晚定了分身方案'))

    def test_empty_session_errors(self):
        r = digest({'session_id': 's2', 'content': ''}); self.assertFalse(r['ok'])

    def test_invalid_input_errors(self):
        r = digest({'content': 'x'}); self.assertFalse(r['ok'])

    def test_secret_line_filtered(self):
        r = digest({'session_id': 's4', 'content': '结论在此\napi_key = sk-xxxx\n要点甲\n要点乙'}); self.assertNotIn('sk-xxxx', r['digest']); self.assertIn('要点甲', r['digest'])

    def test_version_traceable(self):
        r = digest({'session_id': 's5', 'content': '单行会话'}); self.assertTrue(r['ok']); self.assertIn('ops.memory.digest@', r['operator'])



if __name__ == "__main__":
    unittest.main()
