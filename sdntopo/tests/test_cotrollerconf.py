import unittest
import sys
sys.path.insert(1, ".")
import settings
from helpers import telnet_con
from confignodes import configcontroller

class TestController(unittest.TestCase):

    def setUp(self):
        self.cfg = settings.readConfig('topo.cfg')
        self.controller = telnet_con.TelNode(
            self.cfg['controller']['con_ip'], self.cfg['controller']['con_port'])
        self.user = "zerobits"
        self.password = "sdn"
    def test_config(self):
        self.controller.connectAuth(self.user, self.password)
        commands_list = configcontroller.controllerConf(
            self.cfg['controller']['interface'], self.cfg['controller']['ip'], self.cfg['controller']['gw'])
        self.assertEqual(self.controller.execCommand(
            commands_list), True)


if __name__ == "__main__":
    unittest.main()
