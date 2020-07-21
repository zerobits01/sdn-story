#!/usr/bin/python3

import requests
import json

r = requests.get('http://127.0.0.1:8080/wm/core/controller/switches/json', auth=('sdn', 'rocks'))
r.status_code

print(r.headers['content-type'])
print(r.encoding)
print(r.text)

# data = json.loads(r.json())

#print(r.json())

for data in r.json():
    print(data)
