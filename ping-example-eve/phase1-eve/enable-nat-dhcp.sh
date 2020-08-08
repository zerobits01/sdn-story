#!/bin/bash

ip address add 192.168.255.1/24 dev pnet9
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A POSTROUTING -o pnet0 -s 192.168.255.0/24 -j MASQUERADE
systemctl start isc-dhcp-server
