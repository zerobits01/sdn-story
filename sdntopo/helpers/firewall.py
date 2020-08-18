"""
    author: zerobits01
    purpose: helpers for enabling firewall and adding rules
"""
import os

class Rule:
    def __init__(self, sip="", dip="", smac="", dmac="", protocol="ICMP"):
        '''
            this is the intiator of Rule
            at two mac or two ip addresses should be passed and protocol
        '''
        if sip == "" and dip == "" and smac == "" and dmac == "":
            print("[-] enter args!\n need sip or dip dmac or smac")
        else:
            self.sip = sip
            self.dip = dip
            self.smac = smac
            self.dmac = dmac

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
        r = os.system("curl " + url_enabler + " -X PUT") # , auth=('sdn', 'rocks'))
        print(r)
        return r

    def disableFirewall(self):
        '''
            enables the firewall(blocks everything except which rules we add)
        '''
        url_disabler = self.server + ':' + self.port + "/wm/firewall/module/disable/json"
        r = os.system("curl " + url_disabler + " -X PUT") # , auth=('sdn', 'rocks'))
        print(r)
        return r


    def listFirewallRules(self):
        '''
            requests and returns all firewall enabled rules
        '''
        list_rules_url = self.server + ':' + self.port + "/wm/firewall/rules/json"
        response = os.system("curl " + list_rules_url)
        print(response)
        return response

    def addFirewallRule(self, *rules):
        '''
            adds a firewall rule
        '''
        """
        #!/bin/bash
        curl <conotroller-ip>:8080/wm/firewall/module/enable/json -X PUT

        curl -X POST -d '{"src-mac": "50:00:00:04:00:00", "dst-mac": "50:00:00:03:00:00", "nw-proto":"ICMP"}' http://localhost:8080/wm/firewall/rules/json

        curl -X POST -d '{"src-mac": "50:00:00:03:00:00", "dst-mac": "50:00:00:04:00:00", "nw-proto":"ICMP"}' http://localhost:8080/wm/firewall/rules/json
        """
        for rule in rules:
            data = {
                "src-ip":  rule.sip ,
                "dst-ip":  rule.dip ,
                "nw-proto": rule.protocol.upper()
            }
            url_add_rule = self.server + ':' + self.port + "/wm/firewall/rules/json"
            command = f"curl -d \'{data}\' " + url_add_rule + " -X POST"
            print(command)
            r =  os.system(command)# , data=data, auth=('sdn', 'rocks'))
            print(r, "\n\n\n")



