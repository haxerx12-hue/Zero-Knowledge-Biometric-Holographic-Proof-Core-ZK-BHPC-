import unittest
from src.core.zk_engine import ZKProofEngine

class TestZKEngine(unittest.TestCase):
    def test_proof(self):
        engine = ZKProofEngine()
        res = engine.prove([400, 410, 420])
        self.assertEqual(res["certainty"], "100%")

if __name__ == "__main__":
    unittest.main()
