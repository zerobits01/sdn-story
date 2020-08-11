"""
    author: zerobits01
    purpose: configuring emulated servers on my topology in eve
    created: 11-Aug-2020
    modified:11-Aug-2020
"""

# TODO: configuring 4 server nodes


def servertConf(interface, ip, gw):
    return [
        f"ip link set {interface} down",
        f"ip addr add {ip} dev {interface}",
        f"ip link set {interface} up",
        f"ip route add default via {gw} dev {interface}"
    ]

