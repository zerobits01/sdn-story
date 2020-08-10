"""
author : zerobits01
purpose: testing if how to interact with floodlight
created: 10-Aug-2020 12:40
modified: 10-Aug-2020 12:40
"""
import sys
import getpass
import telnetlib
import time

HOST = "172.16.229.131"
PORT = "23"

user = input("Enter your remote account: ")
password = getpass.getpass()

telnetObj = telnetlib.Telnet(HOST,PORT)
time.sleep(2)

telnetObj.write(b"\n")

output = telnetObj.read_until(b"ubuntu login: ")
print(output.decode("ascii"))

telnetObj.write((user + "\n").encode())
telnetObj.read_until(b"Password: ")
telnetObj.write((password + "\n").encode())
telnetObj.read_until(b"zerobits@ubuntu:~$ ")
telnetObj.write(b"echo 2 > test.file\n")
output = telnetObj.read_until(b"zerobits@ubuntu:~$ ")
print(output.decode("ascii"))
print("bye bye! :>")
telnetObj.close()