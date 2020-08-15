"""
    author: zerobits01
    purpose: configuring Open vswitches emulated on my topology in eve
    created: 11-Aug-2020
    modified:11-Aug-2020
"""

# TODO: configuring three ovs switches

def ovsConf(br, protocol, ip, port, ifaces):
    commands = [
        f"echo sdn | sudo -S ovs-vsctl add-br {br}",
        f"sudo ovs-vsctl add-port {br} ens3"
    ]

    commands += [f"sudo ovs-vsctl add-port {br} {interface}" for interface in ifaces]

    commands += [
        f"sudo ovs-vsctl set bridge {br} protocols={protocol}",
        f"sudo ovs-vsctl set-controller tcp:{ip}:{port}"
    ]

    return commands