"""
    author: zerobits01
    purpose: OVS config for ping example
    created at: 4-Aug-2020
    modified at: 4-Aug-2020
"""

import os # we could also use subprocess
import json
import requests
import argparse


argument_parser = argparse.ArgumentParser(
    description="""
        configuring OVS
        gmail : zerobits01@gmail.com
        gitlab: gitlab.com/zerobits01
    """,
    formatter_class=argparse.RawTextHelpFormatter
)

argument_parser.add_argument('-s' , '--server' ,
                        help='enter the server ip here' ,
                            type=str , required=True)


argument_parser.add_argument('-p' , '--port' ,
                        help='enter the server rest api port here' ,
                            type=str , required=True)

argument_parser.add_argument('-i' , '--interface' ,
                        help='interface name' ,
                            type=str, required=True)

argument_parser.add_argument('-i' , '--interface' ,
                        help='interface name e.g ens' ,
                            required=True, type=str)


argument_parser.add_argument('-n' , '--numbers' ,
                        help='interface name e.g ens' ,
                            required=True, type=int, nargs='+')



parsed = argument_parser.parse_args()


if parsed['usage']:
    print(usage)
    return

server = "http://"

if not parsed['server'].__contains__("http://"):
    server += parsed['server']

if not parsed['port']:
    port = "6653"

if not (parsed['mac1'] and parsed['mac2']) :
    print("you didn't enter mac addresses \nenter firewall --usage")


"""
$ ovs-vsctl add-br br0
$ ovs-vsctl add-port br0 eth0
$ ovs-vsctl add-port br0 eth1
$ ovs-vsctl del-port # for deleting port
# don't add the link to the controller and internets to the bridge

set the protocol for each switch:
$ ovs-vsctl set bridge br0 \
    protocols=OpenFlow10,OpenFlow11,OpenFlow12,OpenFlow13

$ ovs-ofctl -O OpenFlow13 dump-flows br0 # to check the flows
$ ovs-vsctl show # to check the switch

$ ovs-vsctl set-controller tcp:<ip-address>:port
have to set up the ip addresses
with ip link and ip addr commands
$ ip link set ensX down
$ ip address add ip/sub dev ensX
$ ip link set ensX up
"""

def createBridge():
    # TODO : adding the bridge
    pass

def addInterfaces():
    # TODO : adding interfaces
    pass

def settingController():
    # TODO : setting controller
    pass

def settingProtocols():
    # TODO : setting protocols
    pass

def setIP():
    # setting an interface ip
    pass