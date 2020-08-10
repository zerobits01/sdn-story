"""
author : zerobits01
purpose: testing how to interact with floodlight
created: 9-Aug-2020 11:07
modified: 9-Aug-2020 11:07
"""

import requests
import sys

enable_url = f"http://{sys.argv[1]}:8080/wm/firewall/module/enable/json"
add_url = f"http://{sys.argv[1]}:8080/wm/firewall/rules/json"

def testEnableFirewall():
    # TODO : request to enable firewall on floodlight
    r = requests.put(enable_url)
    print(r)

def testAddRule():
    # TODO : testing adding a simple rule
    data = {"src-ip": "10.0.0.4/32", "dst-ip": "10.0.0.5/32", "nw-proto":"ICMP"}
    r = requests.post(url=add_url, data=data)
    print(r.content)

def testPrintRules():
    r = requests.get(url=add_url)
    print(r.content)

if __name__ == "__main__":
    testEnableFirewall()
    testAddRule()
    testPrintRules()


# Test Done correctly