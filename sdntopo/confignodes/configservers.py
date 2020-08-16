"""
    author: zerobits01
    purpose: configuring emulated servers on my topology in eve
    created: 11-Aug-2020
    modified:11-Aug-2020
"""

# TODO: configuring 4 server nodes


def servertConf(interface, ip, gw):
    return [
        f"echo sdn | sudo -S ip link set {interface} down",
        f"sudo ip addr add {ip} dev {interface}",
        f"sudo ip link set {interface} up",
        f"sudo ip route add default via {gw} dev {interface}"
    ]

