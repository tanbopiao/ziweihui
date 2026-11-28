# ops.memory.search 沙箱用例
# 运行：python3 tests/test_ops_memory_search.py 或 python -m unittest discover -s tests -v

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from yuanshu import search


class TestSearchOps(unittest.TestCase):
    def test_normal_match(self):
        corpus = {'a1': '第一批三道加固\nnginx 统一面', 'a3': '12月1号开工'}; r = search({'query': '加固', 'corpus': corpus}); self.assertTrue(r['ok']); self.assertEqual(r['total'], 1); self.assertEqual(r['matches'][0]['id'], 'a1')

    def test_secret_hit_filtered(self):
        corpus = {'a2': '密钥行 api_key = sk-xxxx\n普通行照常'}; r = search({'query': 'api', 'corpus': corpus}); self.assertTrue(r['ok']); self.assertEqual(r['total'], 1); self.assertEqual(r['matches'], [])

    def test_secret_query_rejected(self):
        r = search({'query': 'sk-abc token', 'corpus': {}}); self.assertFalse(r['ok'])

    def test_empty_corpus_ok(self):
        r = search({'query': '加固', 'corpus': {}}); self.assertTrue(r['ok']); self.assertEqual(r['matches'], []); self.assertEqual(r['total'], 0)

    def test_invalid_query_errors(self):
        r = search({'corpus': {}}); self.assertFalse(r['ok'])

    def test_version_traceable(self):
        r = search({'query': '开工', 'corpus': {'a3': '12月1号开工'}}); self.assertTrue(r['ok']); self.assertIn('ops.memory.search@', r['operator'])



if __name__ == "__main__":
    unittest.main()
