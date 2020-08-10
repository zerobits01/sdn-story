"""
author : zerobits01
purpose: testing how to interact with eve nodes
created: 9-Aug-2020  11:15
modified: 9-Aug-2020 11:15
"""

import getpass
import subprocess
import os

# HOST = "172.16.229.129"
# user = input("Enter your remote account: ")
# password = getpass.getpass()

print("[+] started")

subprocess.run(["sleep", "2", "echo", "-e", "sdn\n"], stdout=subprocess.PIPE)
t = subprocess.run(['telnet', "-l", "zerobits", "172.16.229.129", "32769"], shell=True, capture_output=True, check=True, stdin=subprocess.PIPE)
# t = subprocess.run(["echo" , "sdn"], stdout=subprocess.PIPE)

print(t.stdout)





"""
import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"ls\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
"""

