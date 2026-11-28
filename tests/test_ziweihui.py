"""紫微讳（ZIWEIHUI）v0.1 单测：三算子＋门面＋legacy 兼容＋边界。"""
import unittest

from ziweihui import Ci, Yan, Xun, Ziweihui


def fp(token):
    import hashlib
    return hashlib.sha256(token.encode()).hexdigest()[:16]


class TestCi(unittest.TestCase):
    def test_issue_returns_token(self):
        t = Ci().issue()
        self.assertIsInstance(t, str)
        self.assertEqual(len(t), 32)

    def test_issued_count_and_fingerprints(self):
        ci = Ci()
        t1 = ci.issue()
        ci.issue()
        self.assertEqual(ci.issued_count, 2)
        self.assertIn(fp(t1), ci.issued_fingerprints())

    def test_no_plaintext_in_ci(self):
        ci = Ci()
        token = ci.issue()
        import json
        self.assertNotIn(token, json.dumps(ci.issued_fingerprints()))


class TestYan(unittest.TestCase):
    def test_first_verify_passes(self):
        yan = Yan()
        t = "a" * 32
        self.assertTrue(yan.verify(t)["granted"])

    def test_second_verify_rejected(self):
        yan = Yan()
        t = "b" * 32
        yan.verify(t)
        self.assertFalse(yan.verify(t)["granted"])

    def test_unknown_token_rejected(self):
        self.assertFalse(Yan().verify("伪讳" * 10 + "x")["granted"])

    def test_result_carries_fingerprint_not_token(self):
        yan = Yan()
        t = "c" * 32
        r = yan.verify(t)
        self.assertEqual(r["fingerprint"], fp(t))
        self.assertNotIn(t, str(r))


class TestXun(unittest.TestCase):
    def test_record_and_filter(self):
        xun = Xun()
        xun.record("grant", "f1", actor="帝座")
        xun.record("verify_pass", "f1")
        self.assertEqual(len(xun.ledger()), 2)
        self.assertEqual(len(xun.ledger("grant")), 1)

    def test_summary(self):
        xun = Xun()
        xun.record("grant", "f1")
        xun.record("verify_pass", "f1")
        xun.record("verify_reject", "f2")
        self.assertEqual(xun.summary(), {"grant": 1, "verify_pass": 1, "verify_reject": 1})


class TestFacade(unittest.TestCase):
    def setUp(self):
        self.op = Ziweihui()

    def test_grant_verify_pass(self):
        t = self.op.grant()
        self.assertTrue(self.op.verify(t)["granted"])

    def test_one_token_one_use(self):
        t = self.op.grant()
        self.op.verify(t)
        self.assertFalse(self.op.verify(t)["granted"])

    def test_verify_before_grant_rejected(self):
        self.assertFalse(self.op.verify("d" * 32)["granted"])

    def test_audit_full_chain(self):
        t = self.op.grant(issuer="测试帝座")
        self.op.verify(t, actor="守卫")
        self.op.verify(t, actor="守卫")  # 拒
        s = self.op.audit_summary()
        self.assertEqual(s, {"grant": 1, "verify_pass": 1, "verify_reject": 1})
        for e in self.op.audit():
            self.assertIn(e["action"], ("grant", "verify_pass", "verify_reject"))
            self.assertTrue(e["ts"])

    def test_audit_never_contains_plaintext(self):
        t = self.op.grant()
        self.op.verify(t)
        self.assertNotIn(t, str(self.op.audit()))
        self.assertIn(fp(t), str(self.op.audit()))

    def test_legacy_describe_unchanged(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "ziweihui")
        self.assertEqual(d["code"], "ZIWEIHUI")
        self.assertEqual(d["mingwen"], "讳出宸极，莫见其全")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))

    def test_legacy_grant_use_unchanged(self):
        t = self.op.grant()
        self.assertTrue(self.op.use(t)["granted"])
        with self.assertRaises(PermissionError):
            self.op.use(t)
        with self.assertRaises(PermissionError):
            self.op.use("伪讳")


if __name__ == "__main__":
    unittest.main()
