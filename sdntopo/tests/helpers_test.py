import unittest
import os, sys
sys.path.insert(1,"/home/zbits/projects/sdn-story/sdntopo")
import sdnhelpers as helpers

valid_ip1     = "192.168.1.1"
valid_ip2     = "10.0.0.1"
invalid_ip    = "10.192.a.2"
valid_port    = "6653"
invalid_port  = "-7"
invalid_port1 = "a236"


class TestStringMethods(unittest.TestCase):

    def test_validip1(self):

        print(f"[!] testcase : {valid_ip1}")
        self.assertEqual(helpers.checkIPAddress(valid_ip1), True)

    def test_validip2(self):
        print(f"[!] testcase : {valid_ip2}")
        self.assertTrue(helpers.checkIPAddress(valid_ip2))

    def test_invalidip(self):
        print(f"[!] testcase : {invalid_ip}")
        self.assertFalse(helpers.checkIPAddress(invalid_ip))

    def test_portcheck(self):
        print(f"[!] testcase : {valid_port}")
        self.assertTrue(helpers.checkPort(valid_port))

    def test_invalid1_portcheck(self):
        print(f"[!] testcase : {invalid_port}")
        self.assertFalse(helpers.checkPort(invalid_port))

    def test_invalid2_portcheck(self):
        print(f"[!] testcase : {invalid_port1}")
        self.assertFalse(helpers.checkPort(invalid_port1))

if __name__ == '__main__':
    unittest.main()