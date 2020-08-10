"""
author : zerobits01
purpose: testing if how to interact with floodlight
created: 10-Aug-2020 12:40
modified: 10-Aug-2020 12:40
"""
import sys
import telnetlib

HOST = "172.16.229.129"
PORT = "32769"

telnetObj = telnetlib.Telnet(HOST,PORT)
output = telnetObj.read_until(b"Escape character is \'^]\'. \n", timeout=5)
# output = telnetObj.read_until(b"\n")
print(output.decode("ascii"))

telnetObj.write(b"zerobits\n")
telnetObj.read_until(b"Password: ")
telnetObj.write(b"sdn\n")
telnetObj.read_until(b"zerobits@ubuntu:~$ ")
telnetObj.write(b"echo 1 > test.file\n")
output = telnetObj.read_until(b"zerobits@ubuntu:~$ ")
print(output.decode("ascii"))
print("bye bye! :>")
telnetObj.close()