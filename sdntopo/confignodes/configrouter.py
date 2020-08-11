"""
    author: zerobits01
    purpose: configuring router emulated on my topology in eve
    created: 11-Aug-2020
    modified:11-Aug-2020
"""

# TODO: configuring router and also enabling nat on it

"""
router config:
fa0 => 10.0.0.1/24 # admin
fa1 => 10.0.1.1/24 # controller
fa2 => 192.168.14.1/24 # internet
fa3 => 10.0.4.1/24 # firewall
fa4 => 10.0.2.1/24 # servers
fa5 => 10.0.3.1/24 # employees
"""

def routerConf():
    return [
        "en",
        "conf t",
        "interface fastEthernet 0/0",
        "ip address 10.0.0.1 255.255.255.0",
        "no shutdown",
        "exit",
        "interface fastEthernet 1/0",
        "ip address 10.0.1.1 255.255.255.0",
        "no shutdown",
        "exit",
        "interface fastEthernet 2/0",
        "ip address 192.168.14.10 255.255.255.0 # also have to set nat for it",
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
        "interface fastEthernet 5/0",
        "ip address 10.0.3.1 255.255.255.0",
        "no shutdown",
        "exit",
        "interface fastEthernet 1/0",
        "ip nat outside",
        "exit",
        "interface fastEthernet 0/0",
        "ip nat inside",
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
        "ip nat inside source static 10.0.255.255 192.168.14.10"
    ]