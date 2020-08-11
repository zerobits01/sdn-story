"""
    author: zerobits01
    purpose: configuring admin emulated machine on my topology in eve
    created: 11-Aug-2020
    modified:11-Aug-2020
"""

# TODO: configuring one admin node


def adminConf(interface, ip, gw):
    return [
        f"ip link set {interface} down",
        f"ip addr add {ip} dev {interface}",
        f"ip link set {interface} up",
        f"ip route add default via {gw} dev {interface}"
    ]