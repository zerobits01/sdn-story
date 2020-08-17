import settings
from helpers import telrouter
from confignodes import configrouter
import unittest
import sys
sys.path.insert(1, ".")


class TestRouter(unittest.TestCase):

    def setUp(self):
        self.cfg = settings.readConfig('topo.cfg')
        self.router = telrouter.TelNode(
            self.cfg['router']['con_ip'], self.cfg['router']['con_port'])

    def test_config(self):
        commands_list = configrouter.routerConf()
        self.assertEqual(self.router.execCommand(
            commands_list).split("\n")[-1], "Router(config)#")


if __name__ == "__main__":
    unittest.main()
