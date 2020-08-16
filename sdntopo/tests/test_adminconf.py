import unittest
import sys
sys.path.insert(1, ".")
import settings
from helpers import telnet_con
from confignodes import configadmin

class TestAdmin(unittest.TestCase):

    def setUp(self):
        self.cfg = settings.readConfig('topo.cfg')
        self.admin = telnet_con.TelNode(
            self.cfg['admin']['con_ip'], self.cfg['admin']['con_port'])
        self.user = "zerobits"
        self.password = "sdn"
    def test_config(self):
        self.admin.connectAuth(self.user, self.password)
        commands_list = configadmin.adminConf(
            self.cfg['admin']['interface'], self.cfg['admin']['ip'], self.cfg['admin']['gw'])
        self.assertEqual(self.admin.execCommand(
            commands_list), True)


if __name__ == "__main__":
    unittest.main()