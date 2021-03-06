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

"""
    Important : this is just a test i know that i have to check the input with regex
"""


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
                        help='interface name e.g ens' ,
                            required=True, type=str, nargs='+')



parsed = argument_parser.parse_args()




server = parsed.server if parsed.server.__contains__("http://") else ( "http://" + parsed.server)


def createBridge():
    if not os.system("ovs-vsctl add-br br0"):
        print("[+] bridge created")
    else:
        print("[-] something went wrong!")
        raise ValueError("[-] bridge couldn't be create")

def addInterfaces():
    if len(parsed['numbers']) == 0 or parsed['interface'] == "":
        raise ValueError('[-] enter args correctly!!')
    for i in parsed['numbers']:
        os.system(f"ovs-vsctl add-port br0 {parsed.interface{i}}")


def settingController():
    # TODO : setting controller
    if not os.system(f"ovs-vsctl set-controller tcp:{server}:{parsed.port}"):
        print("[+] controller has been set")
    else:
        print("[-] something went wrong!")
        raise ValueError("[-] controller couldn't be set")


def settingProtocols():
    if not os.system("ovs-vsctl set bridge br0 protocols=OpenFlow13"):
        print("[+] protocol has been set")
    else:
        print("[-] something went wrong!")
        raise ValueError("[-] protocol couldn't be set")

