import unittest
from threat_detector import get_risk_level


class TestThreatDetector(unittest.TestCase):

    def test_normal_traffic(self):
        self.assertEqual(get_risk_level("normal"), "LOW")

    def test_port_scan(self):
        self.assertEqual(get_risk_level("port_scan"), "MEDIUM")

    def test_brute_force(self):
        self.assertEqual(get_risk_level("brute_force"), "HIGH")

    def test_ddos(self):
        self.assertEqual(get_risk_level("ddos"), "HIGH")

    def test_unknown_traffic(self):
        self.assertEqual(get_risk_level("unknown"), "UNKNOWN")


if __name__ == "__main__":
    unittest.main()