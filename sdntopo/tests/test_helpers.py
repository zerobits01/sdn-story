"""
    author: zerobits01
    purpose: testing helpers module
    created: 10-Aug-2020
    modified: 11-Aug-2020
    description: running terminal should be at parent dir(where sdnhelpers module exists)
"""
import unittest
import sys
sys.path.insert(1, ".")
from helpers import sdnhelpers


class TestHelpers(unittest.TestCase):

    def setUp(self):
        self.valid_ip1     = "192.168.1.1"
        self.valid_ip2     = "10.0.0.1"
        self.invalid_ip    = "10.192.a.2"
        self.valid_port    = "6653"
        self.invalid_port  = "-7"
        self.invalid_port1 = "a236"

    def test_validip1(self):

        print(f"[!] testcase : {self.valid_ip1}")
        self.assertEqual(sdnhelpers.checkIPAddress(self.valid_ip1), True)

    def test_validip2(self):
        print(f"[!] testcase : {self.valid_ip2}")
        self.assertTrue(sdnhelpers.checkIPAddress(self.valid_ip2))

    def test_invalidip(self):
        print(f"[!] testcase : {self.invalid_ip}")
        self.assertFalse(sdnhelpers.checkIPAddress(self.invalid_ip))

    def test_portcheck(self):
        print(f"[!] testcase : {self.valid_port}")
        self.assertTrue(sdnhelpers.checkPort(self.valid_port))

    def test_invalid1_portcheck(self):
        print(f"[!] testcase : {self.invalid_port}")
        self.assertFalse(sdnhelpers.checkPort(self.invalid_port))

    def test_invalid2_portcheck(self):
        print(f"[!] testcase : {self.invalid_port1}")
        self.assertFalse(sdnhelpers.checkPort(self.invalid_port1))

if __name__ == '__main__':
    unittest.main()