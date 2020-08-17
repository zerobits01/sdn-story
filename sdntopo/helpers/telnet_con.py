"""
    author: zerobits01
    purpose: telnet connection and run commands module
    created: 10-Aug-2020
    modified: 10-Aug-2020
"""

import sys
import telnetlib
import time


class TelNode:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.node = telnetlib.Telnet(self.host, self.port)
        self.node.write(b"\n")


    def connectAuth(self, user, password):
        output = self.node.read_until(b"ubuntu login: ")
        print(output.decode("ascii"))
        self.node.write((user + "\n").encode())
        self.node.read_until(b"Password: ")
        self.node.write((password + "\n").encode())
        output = self.node.read_until(b"zerobits@ubuntu:~$ ")
        return output.decode("ascii")

    def execCommand(self, commands):
        '''
            array of string commands should be passed
        '''
        for command in commands:
            self.node.write((command + "\n").encode())
            output = self.node.read_until(b"zerobits@ubuntu:~$ ", timeout=1)
            self.node.write(b"\n")
        output = output.decode("ascii")
        self.node.write(b"\n")
        self.node.write(b"ping -c 15 8.8.8.8\n")
        self.node.write(b"\n")
        if output.__contains__("command not found") or output.__contains__("error"):
            return False
        return True

    def closeNodeConnection(self):
        print(f"bye bye! from host {self.host}:)")
        self.node.close()