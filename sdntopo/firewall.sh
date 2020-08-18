#!/bin/bash

# author: zerobits01
# purpose: enabling and running some rules on floodlight firewall module
#

# 10.0.4.10 => buildserver 10.0.3.14 -/
# 10.0.3.10 => 10.0.3.12 -/
# 10.0.3.11 => 10.0.3.13 -/
# 10.0.3.14 => 3.10, 3.11, 3.12, 3.13
# 10.0.2.10 => * -/

ipport=172.16.229.131:8080
enable_address=/wm/firewall/module/enable/json
add_url=/wm/firewall/rules/json
disable_address=/wm/firewall/module/disable/json
# enabling
curl $ipport$enable_address -X PUT

echo \\n
echo examples
echo curl 172.16.229.131:8080/wm/firewall/module/enable/json -X PUT
echo curl -X POST -d '{"src-ip": "10.0.0.4/32", "dst-ip": "10.0.0.5/32", "nw-proto":"ICMP"}' http://172.16.229.131:8080/wm/firewall/rules/json
echo curl -X POST -d '{"src-ip": "10.0.0.5/32", "dst-ip": "10.0.0.4/32", "nw-proto":"ICMP"}' http://172.16.229.131:8080/wm/firewall/rules/json
echo curl -X POST -d '{"src-ip": "10.0.0.4/32", "dst-ip": "10.0.0.5/32", "nw-proto":"ARP"}' http://172.16.229.131:8080/wm/firewall/rules/json
echo curl -X POST -d '{"src-ip": "10.0.0.5/32", "dst-ip": "10.0.0.4/32", "nw-proto":"ARP"}' http://172.16.229.131:8080/wm/firewall/rules/json

echo \\n

# admin
echo -e admin \\n
curl -X POST -d '{"src-ip": "10.0.1.10/32", "nw-proto":"ICMP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.1.10/32", "nw-proto":"ICMP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"src-ip": "10.0.1.10/32", "nw-proto":"ARP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.1.10/32", "nw-proto":"ARP"}' $ipport$add_url
echo -e admin set up \\n

# django to db
echo -e django to db \\n
curl -X POST -d '{"src-ip": "10.0.3.10/32", "dst-ip": "10.0.3.12/32", "nw-proto":"ICMP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.3.10/32", "src-ip": "10.0.3.12/32", "nw-proto":"ICMP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"src-ip": "10.0.3.10/32", "dst-ip": "10.0.3.12/32", "nw-proto":"ARP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.3.10/32", "src-ip": "10.0.3.12/32", "nw-proto":"ARP"}' $ipport$add_url
echo \\n
echo -e django to db done\\n

# wp to db
echo \\n
echo -e wp to db \\n
curl -X POST -d '{"src-ip": "10.0.3.11/32", "dst-ip": "10.0.3.13/32", "nw-proto":"ICMP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.3.11/32", "src-ip": "10.0.3.13/32", "nw-proto":"ICMP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"src-ip": "10.0.3.11/32", "dst-ip": "10.0.3.13/32", "nw-proto":"ARP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.3.11/32", "src-ip": "10.0.3.13/32", "nw-proto":"ARP"}' $ipport$add_url
echo -e wp to db done \\n

# build to all
echo -e build to all \\n
curl -X POST -d '{"dst-ip": "10.0.3.14/32", "src-ip": "10.0.3.10/32", "nw-proto":"ICMP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.3.14/32", "src-ip": "10.0.3.11/32", "nw-proto":"ICMP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.3.14/32", "src-ip": "10.0.3.12/32", "nw-proto":"ICMP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.3.14/32", "src-ip": "10.0.3.13/32", "nw-proto":"ICMP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.3.10/32", "src-ip": "10.0.3.14/32", "nw-proto":"ICMP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.3.11/32", "src-ip": "10.0.3.14/32", "nw-proto":"ICMP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.3.12/32", "src-ip": "10.0.3.14/32", "nw-proto":"ICMP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.3.13/32", "src-ip": "10.0.3.14/32", "nw-proto":"ICMP"}' $ipport$add_url
echo \\n

curl -X POST -d '{"dst-ip": "10.0.3.14/32", "src-ip": "10.0.3.10/32", "nw-proto":"ARP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.3.14/32", "src-ip": "10.0.3.11/32", "nw-proto":"ARP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.3.14/32", "src-ip": "10.0.3.12/32", "nw-proto":"ARP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.3.14/32", "src-ip": "10.0.3.13/32", "nw-proto":"ARP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.3.10/32", "src-ip": "10.0.3.14/32", "nw-proto":"ARP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.3.11/32", "src-ip": "10.0.3.14/32", "nw-proto":"ARP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.3.12/32", "src-ip": "10.0.3.14/32", "nw-proto":"ARP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.3.13/32", "src-ip": "10.0.3.14/32", "nw-proto":"ARP"}' $ipport$add_url
echo \\n

echo -e build to all done \\n


# emplyee to build
echo -e employee to build\\n
curl -X POST -d '{"dst-ip": "10.0.3.14/32", "src-ip": "10.0.4.10/32", "nw-proto":"ICMP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"src-ip": "10.0.3.14/32", "dst-ip": "10.0.4.10/32", "nw-proto":"ICMP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"dst-ip": "10.0.3.14/32", "src-ip": "10.0.4.10/32", "nw-proto":"ARP"}' $ipport$add_url
echo \\n
curl -X POST -d '{"src-ip": "10.0.3.14/32", "dst-ip": "10.0.4.10/32", "nw-proto":"ARP"}' $ipport$add_url
echo -e employee to build done\\n

# disable and enable
echo -e restarting \\n
curl $ipport$disable_address -X PUT
echo \\n
curl $ipport$enable_address  -X PUT
echo -e restarting done \\n
