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

    def addFirewallRule(self, rule):
        '''
            adds a firewall rule
        '''
        url_add_rule = self.server + ':' + self.port + "/wm/firewall/rules/json"
        r = requests.post(url_add_rule, data=rule, auth=('sdn','rocks'))

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


pusher.addStaticFlow(payload=flow1)
pusher.addStaticFlow(payload=flow2)
pusher.addStaticFlow(payload=flow3)
