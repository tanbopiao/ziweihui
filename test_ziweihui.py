"""紫微讳（ZIWEIHUI）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
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

    def test_grant_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.grant()

    def test_use_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.use(None)


if __name__ == "__main__":
    unittest.main()
