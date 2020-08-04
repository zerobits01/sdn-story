"""
    author: zerobits01
    purpose: setting ip for node
    created at: 4-Aug-2020
    modified at: 4-Aug-2020
"""



import argparse
import os


argument_parser = argparse.ArgumentParser(
    description="""
        setting ip staticlly
        gmail : zerobits01@gmail.com
        gitlab: gitlab.com/zerobits01
    """,
    formatter_class=argparse.RawTextHelpFormatter
)

argument_parser.add_argument('-i' , '--interface' ,
                        help='enter the interface name' ,
                            type=str , required=True)

argument_parser.add_argument('--ip' ,
                        help='enter the ip wacced(with net masc e.g 192.168.1.1/24)' ,
                            type=str , required=True)

parsed = argument_parser.parse_args()

intrface = parsed['interface']
ip = parsed['ip']

def setIP():
    if not os.system(f"ip link set {interface} down"):
        raise ValueError("[-] can not take interface down")
        return
    if not os.system(f"ip address add {ip} dev {interface}"):
        raise ValueError("[-] can not set the ip")
        return
    if not os.system(f"ip link set {interface} up"):
        raise ValueError("[-] can not take interface up")
        return


try:
    setIP()
except e:
    print(e)