"""紫微讳（ZIWEIHUI）算子单测：名帖完整、行为达标、只增不覆盖。"""
import unittest

from ziweihui import Ziweihui


class TestZiweihui(unittest.TestCase):
    def setUp(self):
        self.op = Ziweihui()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "ziweihui")
        self.assertEqual(d["code"], "ZIWEIHUI")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_grant_use_once(self):
        token = self.op.grant()
        self.assertTrue(self.op.use(token)["granted"])
        with self.assertRaises(PermissionError):
            self.op.use(token)
        with self.assertRaises(PermissionError):
            self.op.use("伪讳")


if __name__ == "__main__":
    unittest.main()
