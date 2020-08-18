"""
    author: zerobits01
    purpose: configuring router emulated on my topology in eve
    created: 11-Aug-2020
    modified:11-Aug-2020
"""

# TODO: configuring router and also enabling nat on it

"""
router config:
10.0.1.10/24 # admin
10.0.2.1/24 # tester
10.0.3.1/24 # servers
10.0.4.1/24 # employees
192.168.14.1/24 # internet
"""


def routerConf():
    return [
        "en",
        "conf t",
        "interface fastEthernet 0/0",
        "ip address dhcp",
        "no shutdown",
        "exit",
        "interface fastEthernet 1/0",
        "ip address 10.0.1.1 255.255.255.0",
        "no shutdown",
        "exit",
        "interface fastEthernet 2/0",
        "ip address 10.0.3.1 255.255.255.0",
        "no shutdown",
        "exit",
        "interface fastEthernet 3/0",
        "ip address 10.0.4.1 255.255.255.0",
        "no shutdown",
        "exit",
        "interface fastEthernet 4/0",
        "ip address 10.0.2.1 255.255.255.0",
        "no shutdown",
        "exit",
        "interface fastEthernet 1/0",
        "ip nat inside",
        "exit",
        "interface fastEthernet 0/0",
        "ip nat outside",
        "exit",
        "interface fastEthernet 2/0",
        "ip nat inside",
        "exit",
        "interface fastEthernet 3/0",
        "ip nat inside",
        "exit",
        "interface fastEthernet 4/0",
        "ip nat inside",
        "exit",
        "access-list 1 permit 10.0.0.0 0.0.255.255",
        # "ip nat pool MY_POOL 192.168.255.30 192.168.255.130 netmask 255.255.255.0",
        # "ip nat inside source list 1 static ",
        "ip nat inside source list 1 interface fastEthernet 0/0 overload",
        "exit",
        "write",
        # "write memory"
    ]
