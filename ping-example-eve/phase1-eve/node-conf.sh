#!/bin/bash
sudo ip link set ens3 down
sudo ip addr add $1/24 dev ens3
sudo ip link set ens3 up

