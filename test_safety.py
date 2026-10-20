import unittest
from src.core.safety_guard import IEC60601SafetyGuard

class TestSafety(unittest.TestCase):
    def test_clamp(self):
        self.assertEqual(IEC60601SafetyGuard.clamp_current(300), 210)

if __name__ == "__main__":
    unittest.main()
