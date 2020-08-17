"""
    author: zerobits01
    purpose: configuring floodlight controller
            emulated machine on my topology in eve
    created: 11-Aug-2020
    modified:11-Aug-2020
"""

# TODO: configuring one controller node

def controllerConf(interface, ip, gw):
    return [
        f"echo sdn | sudo -S ip addr add {ip} dev {interface}",
        "\n",
        f"sudo ip route add default via {gw} dev {interface}"
    ]