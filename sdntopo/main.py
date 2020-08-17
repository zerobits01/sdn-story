"""
    author: zerobits01
    purpose: running all configs for project
    created: 11-Aug-2020
    modified: 11-Aug-2020
"""
import sys
sys.path.insert(1, ".")
from confignodes import *
from helpers import *
import settings

class NetworkInitializer:

    def __init__(self, user, passwd):
        self.user = user
        self.password = passwd
        self.cfg = settings.readConfig('topo.cfg')

    def routerSetup(self):
        self.router = telrouter.TelNode(
            self.cfg['router']['con_ip'], self.cfg['router']['con_port'])

    def routerConfig(self):
        commands_list = configrouter.routerConf()
        self.router.execCommand(commands_list)

    def ovsSetup(self):
        self.ovs1 = telnet_con.TelNode(
            self.cfg['ovs1']['con_ip'], self.cfg['ovs1']['con_port'])
        self.ovs2 = telnet_con.TelNode(
            self.cfg['ovs2']['con_ip'], self.cfg['ovs2']['con_port'])
        self.ovs3 = telnet_con.TelNode(
            self.cfg['ovs3']['con_ip'], self.cfg['ovs3']['con_port'])

    def ovsConfig(self):
        self.ovs1.connectAuth(self.user, self.password)
        commands_list = configovs.ovsConf(self.cfg['ovs1']['br'], self.cfg['ovs1']['protocol'],
                                          self.cfg['ovs1']['ip'], self.cfg['ovs1']['port'], [x for x in self.cfg['ovs1']['interfaces'].split(", ")])
        self.ovs1.execCommand(commands_list)

        self.ovs2.connectAuth(self.user, self.password)
        commands_list = configovs.ovsConf(self.cfg['ovs2']['br'], self.cfg['ovs2']['protocol'],
                                          self.cfg['ovs2']['ip'], self.cfg['ovs2']['port'], [x for x in self.cfg['ovs2']['interfaces'].split(", ")])
        self.ovs2.execCommand(commands_list)

        self.ovs3.connectAuth(self.user, self.password)
        commands_list = configovs.ovsConf(self.cfg['ovs3']['br'], self.cfg['ovs3']['protocol'],
                                          self.cfg['ovs3']['ip'], self.cfg['ovs3']['port'], [x for x in self.cfg['ovs3']['interfaces'].split(", ")])
        self.ovs3.execCommand(commands_list)

    def adminSetup(self):
        self.admin = telnet_con.TelNode(
            self.cfg['admin']['con_ip'], self.cfg['admin']['con_port'])

    def adminConfig(self):
        self.admin.connectAuth(self.user, self.password)
        commands_list = configadmin.adminConf(
            self.cfg['admin']['interface'], self.cfg['admin']['ip'], self.cfg['admin']['gw'])
        self.admin.execCommand(commands_list)

    def serversSetup(self):
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

    def serversConfig(self):
        self.django_server.connectAuth(self.user, self.password)
        commands_list = configservers.servertConf(
            self.cfg['django_server']['interface'], self.cfg['django_server']['ip'], self.cfg['django_server']['gw'])
        self.django_server.execCommand(commands_list)

        self.wp_server.connectAuth(self.user, self.password)
        commands_list = configservers.servertConf(
            self.cfg['wp_server']['interface'], self.cfg['wp_server']['ip'], self.cfg['wp_server']['gw'])
        self.wp_server.execCommand(commands_list)

        self.django_db.connectAuth(self.user, self.password)
        commands_list = configservers.servertConf(
            self.cfg['django_db']['interface'], self.cfg['django_db']['ip'], self.cfg['django_db']['gw'])
        self.django_db.execCommand(commands_list)

        self.wp_db.connectAuth(self.user, self.password)
        commands_list = configservers.servertConf(
            self.cfg['wp_db']['interface'], self.cfg['wp_db']['ip'], self.cfg['wp_db']['gw'])
        self.wp_db.execCommand(commands_list)

        self.build_server.connectAuth(self.user, self.password)
        commands_list = configservers.servertConf(
            self.cfg['build_server']['interface'], self.cfg['build_server']['ip'], self.cfg['build_server']['gw'])
        self.build_server.execCommand(commands_list)

    def hostsSetup(self):
        self.host1 = telnet_con.TelNode(self.cfg['host1']['con_ip'], self.cfg['host1']['con_port'])
        self.host2 = telnet_con.TelNode(self.cfg['host2']['con_ip'], self.cfg['host2']['con_port'])

    def hostsConfig(self):
        self.host1.connectAuth(self.user, self.password)
        commands_list = confighosts.hostConf(self.cfg['host1']['interface'], self.cfg['host1']['ip'], self.cfg['host1']['gw'])
        self.host1.execCommand(commands_list)
        self.host2.connectAuth(self.user, self.password)
        commands_list = confighosts.hostConf(self.cfg['host2']['interface'], self.cfg['host2']['ip'], self.cfg['host2']['gw'])
        self.host2.execCommand(commands_list)

    def run(self):
        print("[!] configuring router")
        self.routerSetup()
        self.routerConfig()
        print("[!] configuring OVS switches")
        self.ovsSetup()
        self.ovsConfig()
        print("[!] configuring admin")
        self.adminSetup()
        self.adminConfig()
        print("[!] configuring servers")
        self.serversSetup()
        self.serversConfig()
        print("[!] configuring hosts")
        self.hostsSetup()
        self.hostsConfig()
        print("[+] done!")

    def serversSetupTest(self):
        self.wp_server = telnet_con.TelNode(
            self.cfg['wp_server']['con_ip'], self.cfg['wp_server']['con_port'])
        self.wp_db = telnet_con.TelNode(
            self.cfg['wp_db']['con_ip'], self.cfg['wp_db']['con_port'])
        self.build_server = telnet_con.TelNode(
            self.cfg['build_server']['con_ip'], self.cfg['build_server']['con_port'])
        self.django_db = telnet_con.TelNode(
            self.cfg['django_db']['con_ip'], self.cfg['django_db']['con_port'])

    def serversConfigTest(self):
        self.wp_server.connectAuth(self.user, self.password)
        commands_list = configservers.servertConf(
            self.cfg['wp_server']['interface'], self.cfg['wp_server']['ip'], self.cfg['wp_server']['gw'])
        self.wp_server.execCommand(commands_list)

        self.wp_db.connectAuth(self.user, self.password)
        commands_list = configservers.servertConf(
            self.cfg['wp_db']['interface'], self.cfg['wp_db']['ip'], self.cfg['wp_db']['gw'])
        self.wp_db.execCommand(commands_list)

        self.django_db.connectAuth(self.user, self.password)
        commands_list = configservers.servertConf(
            self.cfg['django_db']['interface'], self.cfg['django_db']['ip'], self.cfg['django_db']['gw'])
        self.django_db.execCommand(commands_list)

        self.build_server.connectAuth(self.user, self.password)
        commands_list = configservers.servertConf(
            self.cfg['build_server']['interface'], self.cfg['build_server']['ip'], self.cfg['build_server']['gw'])
        self.build_server.execCommand(commands_list)

    def hostsSetupTest(self):
        self.host1 = telnet_con.TelNode(self.cfg['host1']['con_ip'], self.cfg['host1']['con_port'])

    def hostsConfigTest(self):
        self.host1.connectAuth(self.user, self.password)
        commands_list = confighosts.hostConf(self.cfg['host1']['interface'], self.cfg['host1']['ip'], self.cfg['host1']['gw'])
        self.host1.execCommand(commands_list)

    def runTest(self):
        print("[!] configuring router")
        self.routerSetup()
        self.routerConfig()
        print("[!] configuring OVS switches")
        self.ovsSetup()
        self.ovsConfig()
        print("[!] configuring admin")
        self.adminSetup()
        self.adminConfig()
        print("[!] configuring servers")
        self.serversSetupTest()
        self.serversConfigTest()
        print("[!] configuring hosts")
        self.hostsSetupTest()
        self.hostsConfigTest()
        print("[+] done!")


net = NetworkInitializer("zerobits", "sdn")
# net.run() # do the configuration completely

if __name__ == "__main__":
    net.runTest()
    while True:
        s = input("enter \"exit\" to exit: ")
        if s == "exit":
            print("bye bye!!")
            break