"""
    author: zerobits01
    purpose: helpers for enabling firewall and adding rules
"""
import requests

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



