"""
    author: zerobits01
    purpose: running all configs for project
    created: 11-Aug-2020
    modified: 11-Aug-2020
"""
import sys
sys.path.insert(1, ".")
import settings
from helpers import *
from confignodes import *


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
        self.host1 = telnet_con.TelNode(
            self.cfg['host1']['con_ip'], self.cfg['host1']['con_port'])
        self.host2 = telnet_con.TelNode(
            self.cfg['host2']['con_ip'], self.cfg['host2']['con_port'])

    def hostsConfig(self):
        self.host1.connectAuth(self.user, self.password)
        commands_list = confighosts.hostConf(
            self.cfg['host1']['interface'], self.cfg['host1']['ip'], self.cfg['host1']['gw'])
        self.host1.execCommand(commands_list)
        self.host2.connectAuth(self.user, self.password)
        commands_list = confighosts.hostConf(
            self.cfg['host2']['interface'], self.cfg['host2']['ip'], self.cfg['host2']['gw'])
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
        self.host1 = telnet_con.TelNode(
            self.cfg['host1']['con_ip'], self.cfg['host1']['con_port'])

    def hostsConfigTest(self):
        self.host1.connectAuth(self.user, self.password)
        commands_list = confighosts.hostConf(
            self.cfg['host1']['interface'], self.cfg['host1']['ip'], self.cfg['host1']['gw'])
        self.host1.execCommand(commands_list)

    def setupFirewall(self):
        '''
            10.0.4.10 => buildserver 10.0.3.14 -/
            10.0.3.10 => 10.0.3.12 -/
            10.0.3.11 => 10.0.3.13 -/
            10.0.3.14 => 3.10, 3.11, 3.12, 3.13
            10.0.2.10 => * -/
        '''
        self.r1 = firewall.Rule(sip="10.0.1.10/32")
        self.r2 = firewall.Rule(dip="10.0.1.10/32")
        self.r3 = firewall.Rule(sip="10.0.4.10/32", dip="10.0.3.14/32")
        self.r4 = firewall.Rule(sip="10.0.3.14/32", dip="10.0.4.10/32")
        self.r5 = firewall.Rule(sip="10.0.3.11/32", dip="10.0.3.13/32")
        self.r6 = firewall.Rule(sip="10.0.3.13/32", dip="10.0.3.11/32")
        self.r7 = firewall.Rule(sip="10.0.3.10/32", dip="10.0.3.12/32")
        self.r8 = firewall.Rule(sip="10.0.3.12/32", dip="10.0.3.10/32")
        self.r9 = firewall.Rule(sip="10.0.3.14/32", dip="10.0.3.10/32")
        self.r10 = firewall.Rule(sip="10.0.3.14/32", dip="10.0.3.11/32")
        self.r11 = firewall.Rule(sip="10.0.3.14/32", dip="10.0.3.12/32")
        self.r12 = firewall.Rule(sip="10.0.3.14/32", dip="10.0.3.10/32")
        self.r13 = firewall.Rule(sip="10.0.3.10/32", dip="10.0.3.14/32")
        self.r14 = firewall.Rule(sip="10.0.3.11/32", dip="10.0.3.14/32")
        self.r15 = firewall.Rule(sip="10.0.3.12/32", dip="10.0.3.14/32")
        self.r16 = firewall.Rule(sip="10.0.3.13/32", dip="10.0.3.14/32")
        self.fw = firewall.FireWall("http://172.16.229.131", port="8080")
        self.fw.enableFirewall()
        self.fw.addFirewallRule(self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.r7,
                                self.r8, self.r9, self.r10, self.r11, self.r12, self.r13, self.r14, self.r15, self.r16)
        self.fw.disableFirewall()
        self.fw.enableFirewall()

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

        # print("[?] setting up floodlight firewall")
        # self.setupFirewall()

net = NetworkInitializer("zerobits", "sdn")
# net.run() # do the configuration completely

if __name__ == "__main__":
    print("""
        first of all do these steps and enter done:
            > ssh root@172.16.229.129 # pass eve
            > ./enable-nat.sh
            also do the basics for router
    """)
    inp = input("enter done to continue: ")
    # if inp == "fw":
    #     net.setupFirewall()
    #     exit(0)
    net.runTest()
    while True:
        s = input("enter \"exit\" to exit: ")
        if s == "exit":
            print("bye bye!!")
            break
