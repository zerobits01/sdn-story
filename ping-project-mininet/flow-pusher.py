#!/usr/bin/python3
'''
    author : zerobits01
    done : for payampardaz@co
    purpose : research and practical
'''
import json
import requests
import argparse


argument_parser = argparse.ArgumentParser(
    description="""
        This is an interaction tool for floodlight done by zerobits01
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

parsed = argument_parser.parse_args()


# HTTP POST data (add flow), HTTP DELETE (for deletion)


# TODO : define Flow Class and using it's ditionary for when we try to send request
class Rule:
    def __init__(self):
        self.in_port: -1
        self.dpid: "00:00:00:00:00:00:00:00"
        self.dl_src: "00:00:00:00:00:00"
        self.dl_dst: "00:00:00:00:00:00"
        self.dl_type: 0
        self.nw_src_prefix: "0.0.0.0"
        self.nw_src_maskbits: 0
        self.nw_dst_prefix: "0.0.0.0"
        self.nw_dst_maskbits: 0
        self.nw_proto: 0
        self.tp_src: 0
        self.tp_dst: 0
        self.any_dpid: "true"
        self.any_in_port: "true"
        self.any_dl_src: "true"
        self.any_dl_dst: "true"
        self.any_dl_type: "true"
        self.any_nw_src: "true"
        self.any_nw_dst: "true"
        self.any_nw_proto: "true"
        self.any_tp_src: "true"
        self.any_tp_dst: "true"
        self.priority: 0
        self.action: "DENY"

    def __init__(self, **kwargs):
        self.in_port: kwargs['in_port']
        self.dpid: kwargs['dpid']
        self.dl_src: kwargs['dl_src']
        self.dl_dst: kwargs['dl_dst']
        self.dl_type: kwargs['dl_type']
        self.nw_src_prefix: kwargs['nw_src_prefix']
        self.nw_src_maskbits: kwargs['nw_src_maskbits']
        self.nw_dst_prefix: kwargs['nw_dst_prefix']
        self.nw_dst_maskbits: kwargs['nw_dst_maskbits']
        self.nw_proto: kwargs['nw_proto']
        self.tp_src: kwargs['tp_src']
        self.tp_dst: kwargs['tp_dst']
        self.any_dpid: kwargs['any_dpid']
        self.any_in_port: kwargs['any_in_port']
        self.any_dl_src: kwargs['any_dl_src']
        self.any_dl_dst: kwargs['any_dl_dst']
        self.any_dl_type: kwargs['any_dl_type']
        self.any_nw_src: kwargs['any_nw_src']
        self.any_nw_dst: kwargs['any_nw_dst']
        self.any_nw_proto: kwargs['any_nw_proto']
        self.any_tp_src: kwargs['any_tp_src']
        self.any_tp_dst: kwargs['any_tp_dst']
        self.priority: kwargs['priority']
        self.action: kwargs['action']

    def getBlockingRule(self):
        self.__init__()
        return self.__dict__

    def getRule(self):
        return self.__dict__


class Flow:

    def __init__(self):
        pass


class GeneralAction:

    def __init__(self, server, port):
        '''
            configs the server ip address
        '''
        self.server = server
        self.port = port
        self.edit_flows = "/wm/staticflowpusher/json"


    def getSwitches(self):
        '''
            get all the switches info
        '''
        r = requests.get(
            'http://127.0.0.1:8080/wm/core/controller/switches/json', auth=('sdn', 'rocks'))
        r.status_code

        print(r.headers['content-type'])
        print(r.encoding)
        print(r.text)

        # data = json.loads(r.json())

        # print(r.json())

        for data in r.json():
            print(data)


class FireWall:

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
        url_add_rule = self.server + ':' + self.port + "/wm/firewall/rules/json"
        r = requests.post(url_add_rule, data=rule, auth=('sdn', 'rocks'))
        print(r)


class StaticFlowPusher(object):

    def __init__(self, server, port):
        '''
            configs the server ip address
        '''
        self.server = server
        self.port = port
        self.edit_flows = "/wm/staticflowpusher/json"



    def addStaticFlow(self, payload):
        '''
            adds static flow to switches
        '''
        r = requests.post(self.server + ':' + self.port +
                          self.edit_flows, json=payload,  auth=('sdn', 'rocks'))
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
        flows_list_url = "/wm/staticflowpusher/list/" + switch + "/json "


flow1 = {
    'switch': "00:00:00:00:00:00:00:01",
    "name": "flow_mod_1",
    "cookie": 0,
    "priority": "32768",
    "in_port": "3",
    "src-ip": "10.0.0.5",
    "dst-ip": "10.0.0.4",
    "active": "true",
    "actions": "output=2"
}

flow2 = {
    "switch": "00:00:00:00:00:00:00:01",
    "name": "flow_mod_1",
    "cookie": "0",
    "priority": "32768",
    "in_port": "2",
    "src-ip": "10.0.0.4",
    "dst-ip": "10.0.0.5",
    "active": "true",
    "actions": "output=3"
}


flow3 = {
    'switch': "00:00:00:00:00:00:00:01",
    "name": "flow_mod_1",
    "cookie": "0",
    "priority": "32768",
    "in_port": "1",
    "src-ip": "10.0.0.4",
    "dst-ip": "10.0.0.5",
    "active": "true",
    "actions": "Deny"
}


# pusher.addStaticFlow(payload=flow1)
# pusher.addStaticFlow(payload=flow2)
# pusher.addStaticFlow(payload=flow3)

# because icmp is a high level protocol(higher than 2 we can not block it with flows we have to do it with firewall)
# so first we have to block all packet types then just enable ping
rule1 = {"dst-mac": "00:00:00:00:00:04",
         "src-ip": "00:00:00:00:00:05",
         "nw-proto": "ICMP",
         "action": "DENY"
         }

rule2 = {"src-ip": "10.0.0.4",
         "dst-ip": "10.0.0.5",
         "action": "DENY"
         }

rule0 = {"dst-ip": "10.0.0.7/32",
         "dst-ip": "10.0.0.3/32",
         "nw-proto": "ICMP",
         "action": "DENY"
         }



pusher.enableFirewall()

# pusher.addFirewallRule(rule0)
# pusher.addFirewallRule(rule)
# pusher.addFirewallRule(rule1)
# pusher.addFirewallRule(rule2)
pusher.addFirewallRule(Rule().getBlockingRule())


pusher.listFirewallRules()


# curl_request = ""


if not parsed['server'].__contains__("http://"):
    parsed['server'] = "http://" + parsed['server']

if parsed['port'].isnumeric():
    flow_pusher = StaticFlowPusher(parsed['server'], parsed['port'])
    firewall = FireWall(parsed['server'], parsed['port'])
    general_usage = GeneralAction(parsed['server'], parsed['port'])
else :
    print("input data is not correct! :(")