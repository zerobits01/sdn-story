"""
    author: zerobits01
    purpose: testing telnet class
    created: 11-Aug-2020
    modified: 11-Aug-2020
    description: running terminal should be at parent dir(where telnet module exists)
    note: always tests run in order of alphabet
"""
import unittest
import sys
sys.path.insert(1, ".")
from helpers.telnet_con import TelNode

class TestTelnet(unittest.TestCase):

    def setUp(self):
        self.host = "172.16.229.129"
        self.port = 32769
        self.newnode = TelNode(self.host, self.port)
        self.user = "zerobits"
        self.password = "sdn"
        self.commands = ["echo hello zerobits!!"]

    def test_auth(self):
        print(f"[!] testcase : host={self.host} & port={self.port}")
        self.assertEqual(self.newnode.connectAuth(self.user, self.password).__contains__("zerobits@ubuntu:~$ "), True)

    def test_execution(self):
        self.assertNotEqual(self.newnode.execCommand(self.commands), True)
if __name__ == "__main__":
    unittest.main()
