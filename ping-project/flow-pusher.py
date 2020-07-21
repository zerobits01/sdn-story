#!/usr/bin/python3
'''
    author : zerobits01
    done : for payampardaz@co
    purpose : research and practical
'''
import json
import requests


# HTTP POST data (add flow), HTTP DELETE (for deletion) 


# TODO : define Flow Class and using it's ditionary for when we try to send request


class StaticFlowPusher(object):
  
    def __init__(self, server, port):
        '''
            configs the server ip address
        '''
        self.server = server
        self.port = port
        self.edit_flows = "/wm/staticflowpusher/json"


    def enableFirewall(self):
        '''
            enables the firewall(blocks everything except which rules we add)
        '''
        url_enabler = self.server + ':' + self.port + "/wm/firewall/module/enable/json"
        r = requests.put(url_enabler, auth=('sdn','rocks'))
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
        url_add_rule = self.server + ':' + self.port + "/wm/firewall/rules/json"
        r = requests.post(url_add_rule, data=rule, auth=('sdn','rocks'))
        print(r)


    def getSwitches(self):
        '''
            get all the switches info
        '''
        r = requests.get('http://127.0.0.1:8080/wm/core/controller/switches/json', auth=('sdn', 'rocks'))
        r.status_code

        print(r.headers['content-type'])
        print(r.encoding)
        print(r.text)

        # data = json.loads(r.json())

        #print(r.json())

        for data in r.json():
            print(data)


    def addStaticFlow(self, payload):
        '''
            adds static flow to switches
        '''
        r = requests.post(self.server + ':'  + self.port + self.edit_flows, json=payload,  auth=('sdn','rocks'))
        print(r)




    def removeFlow(self):
        '''
            removes a flow with flow name
        '''

        # TODO : add flow deleter
        pass


    def listFlowsOfSwitch(self, switch):
        '''
            lists all statics flows of a switch
        '''
        # TODO : add flows lister
        flows_list_url = "/wm/staticflowpusher/list/" + switch  + "/json "

pusher = StaticFlowPusher('http://127.0.0.1', '8080')
  

flow1 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow_mod_1",
    "cookie":"0",
    "priority":"32768",
    "in_port":"3",
    "src-ip":"10.0.0.5",
    "dst-ip":"10.0.0.4",
    "active":"true",
    "actions":"output=2"
}

flow2 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow_mod_1",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "src-ip":"10.0.0.4",
    "dst-ip":"10.0.0.5",
    "active":"true",
    "actions":"output=3"
}


flow3 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow_mod_1",
    "cookie":"0",
    "priority":"32768",
    "in_port":"1",
    "src-ip":"10.0.0.4",
    "dst-ip":"10.0.0.5",
    "active":"true",
    "actions":""
}


# pusher.addStaticFlow(payload=flow1)
# pusher.addStaticFlow(payload=flow2)
# pusher.addStaticFlow(payload=flow3)

# because icmp is a high level protocol(higher than 2 we can not block it with flows we have to do it with firewall)
# so first we have to block all packet types then just enable ping
rule1 = { "dst-mac": "00:00:00:00:00:04", 
        "src-ip": "00:00:00:00:00:05",
        "nw-proto": "ICMP",
    "action" : "DENY" 
}

rule2 = { "src-ip": "10.0.0.4", 
    "dst-ip": "10.0.0.5", 
    "action" : "DENY" 
}

rule0 = { "dst-ip": "10.0.0.7/32", 
    "dst-ip": "10.0.0.3/32", 
    "nw-proto" : "ICMP",
    "action" : "DENY" 
}


rule = {'ruleid': -1139295682, 'dpid': '00:00:00:00:00:00:00:00', 'in_port': -1, 'dl_src': '00:00:00:00:00:00', 'dl_dst': '00:00:00:00:00:00', 'dl_type': 0, 'nw_src_prefix': '0.0.0.0', 'nw_src_maskbits': 0, 'nw_dst_prefix': '0.0.0.0', 'nw_dst_maskbits': 0, 'nw_proto': 0, 'tp_src': 0, 'tp_dst': 0, 'any_dpid': True, 'any_in_port': True, 'any_dl_src': True, 'any_dl_dst': True, 'any_dl_type': True, 'any_nw_src': True, 'any_nw_dst': True, 'any_nw_proto': True, 'any_tp_src': True, 'any_tp_dst': True, 'priority': 0, 'action': 'DENY'}


block_rule = {
"dpid":"00:00:00:00:00:00:00:00",
"in_port":-1,"dl_src":"00:00:00:00:00:00",
"dl_dst":"00:00:00:00:00:00",
"dl_type":0,
"nw_src_prefix":"0.0.0.0",
"nw_src_maskbits":0,
"nw_dst_prefix":"0.0.0.0",
"nw_dst_maskbits":0,
"nw_proto":0,"tp_src":0,
"tp_dst":0,
"any_dpid":"true",
"any_in_port":"true",
"any_dl_src":"true",
"any_dl_dst":"true",
"any_dl_type":"true",
"any_nw_src":"true",
"any_nw_dst":"true",
"any_nw_proto":"true",
"any_tp_src":"true",
"any_tp_dst":"true",
"priority":0,
"action":"DENY"
}


pusher.enableFirewall()

# pusher.addFirewallRule(rule0)
# pusher.addFirewallRule(rule)
# pusher.addFirewallRule(rule1)
# pusher.addFirewallRule(rule2)
pusher.addFirewallRule(block_rule)


pusher.listFirewallRules()



# curl_request = ""
