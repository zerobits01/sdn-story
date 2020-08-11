"""
    author: zerobits01
    purpose: testing helpers module
    created: 10-Aug-2020
    modified: 11-Aug-2020
    description: running terminal should be at parent dir(where sdnhelpers module exists)
"""
import unittest
import os, sys
sys.path.insert(1,".")
import sdnhelpers as helpers



class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.valid_ip1     = "192.168.1.1"
        self.valid_ip2     = "10.0.0.1"
        self.invalid_ip    = "10.192.a.2"
        self.valid_port    = "6653"
        self.invalid_port  = "-7"
        self.invalid_port1 = "a236"

    def test_validip1(self):

        print(f"[!] testcase : {self.valid_ip1}")
        self.assertEqual(helpers.checkIPAddress(self.valid_ip1), True)

    def test_validip2(self):
        print(f"[!] testcase : {self.valid_ip2}")
        self.assertTrue(helpers.checkIPAddress(self.valid_ip2))

    def test_invalidip(self):
        print(f"[!] testcase : {self.invalid_ip}")
        self.assertFalse(helpers.checkIPAddress(self.invalid_ip))

    def test_portcheck(self):
        print(f"[!] testcase : {self.valid_port}")
        self.assertTrue(helpers.checkPort(self.valid_port))

    def test_invalid1_portcheck(self):
        print(f"[!] testcase : {self.invalid_port}")
        self.assertFalse(helpers.checkPort(self.invalid_port))

    def test_invalid2_portcheck(self):
        print(f"[!] testcase : {self.invalid_port1}")
        self.assertFalse(helpers.checkPort(self.invalid_port1))

if __name__ == '__main__':
    unittest.main()