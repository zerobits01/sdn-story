import unittest
import sys
sys.path.insert(1, ".")
from helpers import telnet_con
from confignodes import configovs
import settings

class TestOVS(unittest.TestCase):

    def setUp(self):
        print("start testing")
        self.cfg = settings.readConfig('topo.cfg')
        self.ovs1 = telnet_con.TelNode(
            self.cfg['ovs1']['con_ip'], self.cfg['ovs1']['con_port'])
        self.ovs2 = telnet_con.TelNode(
            self.cfg['ovs2']['con_ip'], self.cfg['ovs2']['con_port'])
        self.ovs3 = telnet_con.TelNode(
            self.cfg['ovs3']['con_ip'], self.cfg['ovs3']['con_port'])
        self.user = "zerobits"
        self.password = "sdn"

    def test_configovs1(self):
        print(self.cfg['ovs1']['con_ip'], self.cfg['ovs1']['con_port'])
        self.ovs1.connectAuth(self.user, self.password)
        commands_list = configovs.ovsConf(self.cfg['ovs1']['br'], self.cfg['ovs1']['protocol'],
                                          self.cfg['ovs1']['ip'], self.cfg['ovs1']['port'], [x for x in self.cfg['ovs1']['interfaces'].split(", ")])
        self.assertEqual(self.ovs1.execCommand(
            commands_list), True)

    def test_configovs2(self):
        print(self.cfg['ovs2']['con_ip'], self.cfg['ovs2']['con_port'])
        self.cfg['ovs2']['con_ip'], self.cfg['ovs2']['con_port']
        self.ovs2.connectAuth(self.user, self.password)
        commands_list = configovs.ovsConf(self.cfg['ovs2']['br'], self.cfg['ovs2']['protocol'],
                                          self.cfg['ovs2']['ip'], self.cfg['ovs2']['port'], [x for x in self.cfg['ovs2']['interfaces'].split(", ")])
        self.assertEqual(self.ovs2.execCommand(
            commands_list), True)

    def test_configovs3(self):
        print(self.cfg['ovs3']['con_ip'], self.cfg['ovs3']['con_port'])
        self.cfg['ovs3']['con_ip'], self.cfg['ovs3']['con_port']
        self.ovs3.connectAuth(self.user, self.password)
        commands_list = configovs.ovsConf(self.cfg['ovs3']['br'], self.cfg['ovs3']['protocol'],
                                          self.cfg['ovs3']['ip'], self.cfg['ovs3']['port'], [x for x in self.cfg['ovs3']['interfaces'].split(", ")])
        self.assertEqual(self.ovs3.execCommand(
            commands_list), True)


if __name__ == "__main__":
    unittest.main()
