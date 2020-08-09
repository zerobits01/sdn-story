"""
    author: zerobits01
    purpose: enabling firewall, giving access to just two nodes with entered mac
    created at: 4-Aug-2020
    modified at: 9-Aug-2020
"""

import argparse
import json
import requests


usage = """
    firewall.py --enable
    firewall.py --list
    firewall.py --addrule --smac <mac1> --dmac <mac2> --proto <icmp>
    firewall.py --addrule --sip <ip1> --dip <ip2> --proto <icmp>
"""

argument_parser = argparse.ArgumentParser(
    description="""
        enabling firewall for the ping project
        gmail : zerobits01@gmail.com
        gitlab: gitlab.com/zerobits01
    """,
    formatter_class=argparse.RawTextHelpFormatter
)

argument_parser.add_argument('-s' , '--server' ,
                        help='enter the server ip here' ,
                            type=str)


argument_parser.add_argument('-p' , '--port' ,
                        help='enter the server rest api port here' ,
                            type=str)

argument_parser.add_argument('--smac' ,
                        help='enter the source mac address' ,
                            type=str)

argument_parser.add_argument('--dmac' ,
                        help='enter the destination mac address' ,
                            type=str)

argument_parser.add_argument('--sip' ,
                        help='enter the source ip address' ,
                            type=str)

argument_parser.add_argument('--dip' ,
                        help='enter the destination ip address' ,
                            type=str)

argument_parser.add_argument('--protocol' ,
                        help='enter the protocol here' ,
                            type=str, required=True)

argument_parser.add_argument('-u' , '--usage' ,
                        help='print the examples' ,
                            action='store_const', const=True, default=False)

argument_parser.add_argument('-e' , '--enable' ,
                        help='enable firewall' ,
                            action="store_const", const=True, default=False)


argument_parser.add_argument('-l' , '--list' ,
                        help='list firewall rules' ,
                            action="store_const", const=True, default=False)


argument_parser.add_argument('-a' , '--addrule' ,
                        help='enable firewall' ,
                            action="store_const", const=True, default=False)



parsed = argument_parser.parse_args()

'''
    i know that i have to check the inputs but i didn't have enough time
    i did just try to do it as simplest as possible
'''


class Rule:

    def __init__(self, sip, dip, smac, dmac, protocol):
        '''
            this is the intiator of Rule
            at two mac or two ip addresses should be passed and protocol
        '''
        if sip and dip:
            self.sip = sip
            self.dip = dip
        elif smac and dmac:
            self.smac = smac
            self.dmac = dmac
        else:
            print("[-] enter args!\nrun command : firewall-enable --usage")

        self.protocol = protocol


class FireWall:

    def __init__(self, server, port):
        '''
            configs the server ip address
        '''
        self.server = server
        self.port = port

    def enableFirewall(self):
        '''
            enables the firewall(blocks everything except which rules we add)
        '''
        url_enabler = self.server + ':' + self.port + "/wm/firewall/module/enable/json"
        r = requests.put(url_enabler, auth=('sdn', 'rocks'))
        print(r)
        return r

    def listFirewallRules(self):
        '''
            requests and returns all firewall enabled rules
        '''
        list_rules_url = self.server + ':' + self.port + "/wm/firewall/rules/json"
        response = requests.get(list_rules_url)
        print(response.json())
        return response

    def addFirewallRule(self, rule):
        '''
            adds a firewall rule
        '''
        """
        #!/bin/bash
        curl <conotroller-ip>:8080/wm/firewall/module/enable/json -X PUT

        curl -X POST -d '{"src-mac": "50:00:00:04:00:00", "dst-mac": "50:00:00:03:00:00", "nw-proto":"ICMP"}' http://localhost:8080/wm/firewall/rules/json

        curl -X POST -d '{"src-mac": "50:00:00:03:00:00", "dst-mac": "50:00:00:04:00:00", "nw-proto":"ICMP"}' http://localhost:8080/wm/firewall/rules/json
        """
        data = {}
        if rule.smac and rule.dmac:
            data = {
                "src-mac": rule.smac,
                "dst-mac": rule.dmac,
                "nw-proto": rule.proto.to_upper()
            }
        else:
            data = {
                "src-ip": rule.sip,
                "dst-ip": rule.dip,
                "nw-proto": rule.proto.to_upper()
            }
        url_add_rule = self.server + ':' + self.port + "/wm/firewall/rules/json"
        r = requests.post(url_add_rule, data=data, auth=('sdn', 'rocks'))
        print(r)
        return r





if parsed.server.__contains__("http://"):
    server = parsed.server
else:
    server = "http://" + parsed.server


if not parsed.port:
    port = "8080"
else:
    port = parsed.port

fw = FireWall(server, port)

if parsed.usage:
    print(usage)
    exit(0)

if parsed.enable:
    if fw.enableFirewall().status_code == 200:
        print("[+] enabled! :)")
    else:
        print("[-] something went wrong! :(")

if parsed.addrule:
    rule = Rule(sip=parsed.sip, dip=parsed.dip, smac=parsed.smac, dmac=parsed.dmac, protocol=parsed.protocol)


if parsed.list:
    fw.listFirewallRules()
    exit(0)

# test : python3 firewall-enable.py --enable --list --smac "00:00:00:00:00:01" --dmac "00:00:00:00:00:02" --protocol "ICMP" --server 172.16.229.131 --port 8080