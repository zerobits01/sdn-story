#!/bin/bash

sudo ovs-vsctl add-br br0
sudo ovs-vsctl add-port br0 ens4
sudo ovs-vsctl add-port br0 ens5
sudo ovs-vsctl add-port br0 ens6
sudo ovs-vsctl add-port br0 ens7
sudo ovs-vsctl add-port br0 ens8

sudo ovs-vsctl set bridge br0 protocols=OpenFlow13
sudo ovs-vsctl set-controller br0 tcp:$1:$2

