

def adminConf(interface, ip, gw):
    return [
        "echo sdn | sudo -S ifconfig\n",
        "sudo su",
        f"cat << EOF >> /etc/network/interfaces\n",
        f"auto {interface}\nallow-hotplug {interface}\niface {interface} inet static\n\taddress {ip}\n\tgateway {gw}\nEOF\n",
        "systemctl restart networking\n"
    ]

"""
another way :
> echo sdn | sudo -S cat << EOF >> test.test\\nauto ens3\\nallow-hotplug ens3\\niface ens3 inet staticn\\n\\taddress 10.0.1.10/24\\n\\tgateway 10.0.1.1\\nEOF\\n
> sudo systemctl restart networking\n
"""