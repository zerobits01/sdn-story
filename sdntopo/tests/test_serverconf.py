import unittest
import sys
sys.path.insert(1, ".")
import settings
from helpers import telnet_con
from confignodes import configservers

class TestServer(unittest.TestCase):

    def setUp(self):
        self.cfg = settings.readConfig('topo.cfg')
        self.django_server = telnet_con.TelNode(
            self.cfg['django_server']['con_ip'], self.cfg['django_server']['con_port'])
        self.wp_server = telnet_con.TelNode(
            self.cfg['wp_server']['con_ip'], self.cfg['wp_server']['con_port'])
        self.wp_db = telnet_con.TelNode(
            self.cfg['wp_db']['con_ip'], self.cfg['wp_db']['con_port'])
        self.build_server = telnet_con.TelNode(
            self.cfg['build_server']['con_ip'], self.cfg['build_server']['con_port'])
        self.django_db = telnet_con.TelNode(
            self.cfg['django_db']['con_ip'], self.cfg['django_db']['con_port'])

        self.user = "zerobits"
        self.password = "sdn"


    def test_django_server_config(self):
        print("[!] configuring django server")
        print(self.cfg['django_server']['con_ip'], self.cfg['django_server']['con_port'])
        self.django_server.connectAuth(self.user, self.password)
        commands_list = configservers.servertConf(
            self.cfg['django_server']['interface'], self.cfg['django_server']['ip'], self.cfg['django_server']['gw'])
        self.assertEqual(self.django_server.execCommand(
            commands_list), True)


    def test_wp_server_config(self):
        print("[!] configuring wp server")
        print(self.cfg['wp_server']['con_ip'], self.cfg['wp_server']['con_port'])
        self.wp_server.connectAuth(self.user, self.password)
        commands_list = configservers.servertConf(
            self.cfg['wp_server']['interface'], self.cfg['wp_server']['ip'], self.cfg['wp_server']['gw'])
        self.assertEqual(self.wp_server.execCommand(
            commands_list), True)

    def test_django_db_config(self):
        print("[!] configuring django db server")
        print(self.cfg['django_db']['con_ip'], self.cfg['django_db']['con_port'])
        self.django_db.connectAuth(self.user, self.password)
        commands_list = configservers.servertConf(
            self.cfg['django_db']['interface'], self.cfg['django_db']['ip'], self.cfg['django_db']['gw'])
        self.assertEqual(self.django_db.execCommand(
            commands_list), True)

    def test_wp_db_config(self):
        print("[!] configuring wp db server")
        print(self.cfg['wp_db']['con_ip'], self.cfg['wp_db']['con_port'])
        self.wp_db.connectAuth(self.user, self.password)
        commands_list = configservers.servertConf(
            self.cfg['wp_db']['interface'], self.cfg['wp_db']['ip'], self.cfg['wp_db']['gw'])
        self.assertEqual(self.wp_db.execCommand(
            commands_list), True)

    def test_build_server_config(self):
        print("[!] configuring build server")
        print(self.cfg['build_server']['con_ip'], self.cfg['build_server']['con_port'])
        self.build_server.connectAuth(self.user, self.password)
        commands_list = configservers.servertConf(
            self.cfg['build_server']['interface'], self.cfg['build_server']['ip'], self.cfg['build_server']['gw'])
        self.assertEqual(self.build_server.execCommand(
            commands_list), True)


if __name__ == "__main__":
    unittest.main()