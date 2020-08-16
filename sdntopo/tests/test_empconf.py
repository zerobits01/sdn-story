import unittest
import sys
sys.path.insert(1,".")
from confignodes import confighosts
from helpers import telnet_con
import settings



class TestEmp(unittest.TestCase):

    def setUp(self):
        self.cfg = settings.readConfig('topo.cfg')
        self.host1 = telnet_con.TelNode(self.cfg['host1']['con_ip'], self.cfg['host1']['con_port'])
        self.host2 = telnet_con.TelNode(self.cfg['host2']['con_ip'], self.cfg['host2']['con_port'])
        self.user = "zerobits"
        self.password = "sdn"

    def test_host1_config(self):
        print(self.cfg['host1']['con_ip'], self.cfg['host1']['con_port'])
        self.host1.connectAuth(self.user, self.password)
        commands_list = confighosts.hostConf(self.cfg['host1']['interface'], self.cfg['host1']['ip'], self.cfg['host1']['gw'])
        self.assertEqual(self.host1.execCommand(commands_list),True)

    def test_host2_config(self):
        print(self.cfg['host2']['con_ip'], self.cfg['host2']['con_port'])
        self.host2.connectAuth(self.user, self.password)
        commands_list = confighosts.hostConf(self.cfg['host2']['interface'], self.cfg['host2']['ip'], self.cfg['host2']['gw'])
        self.assertEqual(self.host2.execCommand(commands_list),True)


if __name__ == "__main__":
    unittest.main()