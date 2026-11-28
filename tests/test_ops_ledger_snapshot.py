# ops.ledger.snapshot 沙箱用例
# 运行：python3 tests/test_ops_ledger_snapshot.py 或 python -m unittest discover -s tests -v

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from yuanshu import snapshot


class TestSnapshotOps(unittest.TestCase):
    def test_total_and_by_type(self):
        entries = [{'type': 'deploy', 'timestamp': '2026-11-28T20:00:00+08:00'}, {'type': 'deploy', 'timestamp': '2026-11-27T20:00:00+08:00'}, {'type': 'audit', 'timestamp': '2026-11-28T21:00:00+08:00'}, {'timestamp': '2026-11-26T20:00:00+08:00'}]; r = snapshot({'entries': entries}); snap = r['snapshot']; self.assertTrue(r['ok']); self.assertEqual(snap['total'], 4); self.assertEqual(snap['by_type']['deploy'], 2); self.assertEqual(snap['by_type']['未分类'], 1)

    def test_latest_entry(self):
        entries = [{'type': 'deploy', 'timestamp': '2026-11-28T20:00:00+08:00'}, {'type': 'audit', 'timestamp': '2026-11-28T21:00:00+08:00'}]; r = snapshot({'entries': entries}); self.assertEqual(r['snapshot']['latest']['type'], 'audit')

    def test_empty_ledger_ok(self):
        r = snapshot({'entries': []}); self.assertTrue(r['ok']); self.assertEqual(r['snapshot']['total'], 0); self.assertIsNone(r['snapshot']['latest'])

    def test_invalid_entries_errors(self):
        r = snapshot({'entries': 'bad'}); self.assertFalse(r['ok'])

    def test_version_traceable(self):
        r = snapshot({'entries': []}); self.assertIn('ops.ledger.snapshot@', r['operator'])



if __name__ == "__main__":
    unittest.main()
