"""
    author: zerobits01
    purpose: configuring Open vswitches emulated on my topology in eve
    created: 11-Aug-2020
    modified:11-Aug-2020
"""

# TODO: configuring three ovs switches

def ovsConf(br, protocol, ip, port, ifaces, iip=None, interface=None, gw=None):
    commands = [
        # f"echo sdn | sudo -S ip addr add {iip} dev {interface}",
        # "\n",
        # f"sudo ip route add default via {gw} dev {interface}",
        f"echo sdn | sudo -S ovs-vsctl add-br {br}\n",
    ]

    commands += [f"sudo ovs-vsctl add-port {br} {interface}\n" for interface in ifaces]

    commands += [
        f"sudo ovs-vsctl set bridge {br} protocols={protocol}\n",
        f"sudo ovs-vsctl set-controller {br} tcp:{ip}:{port}\n"
    ]

    return commands