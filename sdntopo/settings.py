"""
    author: zerobits01
    purpose: config file custom lib for handling IP and default route addresses
    created: 10-Aug-2020
    modified: 10-Aug-2020
"""

import configparser

cfg = configparser.ConfigParser()


config_example = '''
[host1]
con_ip = 172.16.229.129
con_port=32775
interface = ens3
ip = 10.0.3.10/24
gw = 10.0.3.1

[host2]
con_ip = 172.16.229.129
con_port=32773
interface = ens3
ip = 10.0.3.11/24
gw = 10.0.3.1

[admin]
con_ip = 172.16.229.129
con_port=32772
interface = ens3
ip = 10.0.0.10/24
gw = 10.0.0.1


[controller]
con_ip = 172.16.229.129
con_port=32781
interface = ens3
ip = 10.0.1.10/24
gw = 10.0.1.1

[ovs1]
con_ip = 172.16.229.129
con_port=32769
br = br0
interfaces = ens3, ens4, ens5, ens6, ens7, ens8, ens9
ip = 172.16.229.131
protocol = OpenFlow13
port = 6653

[ovs2]
con_ip = 172.16.229.129
con_port=32770
br = br0
interfaces = ens3, ens4, ens5, ens6, ens7, ens8, ens9
ip = 172.16.229.131
protocol = OpenFlow13
port = 6653

[ovs3]
con_ip = 172.16.229.129
con_port=32771
br = br0
interfaces = ens3, ens4, ens5, ens6, ens7, ens8, ens9
protocol = OpenFlow13
ip = 172.16.229.131
port = 6653


[django_server]
con_ip = 172.16.229.129
con_port=32779
interface = ens3
ip = 10.0.2.10/24
gw = 10.0.2.1

[wp_server]
con_ip = 172.16.229.129
con_port=32780
interface = ens3
ip = 10.0.2.11/24
gw = 10.0.2.1

[djangoDB_server]
con_ip = 172.16.229.129
con_port=32776
interface = ens3
ip = 10.0.2.12/24
gw = 10.0.2.1

[wpDB_server]
con_ip = 172.16.229.129
con_port=32777
interface = ens3
ip = 10.0.2.13/24
gw = 10.0.2.1

[build_server]
con_ip = 172.16.229.129
con_port=32778
interface = ens3
ip = 10.0.2.14/24
gw = 10.0.2.1

'''


def readConfig(config_file):
    '''
        reads config file from the topo.cfg and returns the dictionary
    '''
    cfg.read(config_file)
    return cfg




if __name__ == "__main__":
    try:
        dct = readConfig('topo.cfg')
        print(dct['server']['ip'])
    except Exception as e:
        print(e)
        with open("topo.cfg.example", "w") as config_file:
            print("[!] rename it to topo.cfg.example to topo.cfg")
            config_file.writelines(config_example)
