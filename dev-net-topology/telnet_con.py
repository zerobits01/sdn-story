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
        self.node = None

    def connectAuth(self, user, password):
        self.node = telnetlib.Telnet(self.host, self.port)
        time.sleep(1)
        self.node.write(b"\n")

        output = self.node.read_until(b"ubuntu login: ")
        print(output.decode("ascii"))

        self.node.write((user + "\n").encode())
        self.node.read_until(b"Password: ")
        self.node.write((password + "\n").encode())


    def execCommand(self, commands):
        '''
            array of string commands should be passed
        '''
        self.node.read_until(b"zerobits@ubuntu:~$ ")
        for command in commands:
            self.node.write(command.encode())
        output = self.node.read_until(b"zerobits@ubuntu:~$ ")
        print(output.decode("ascii"))

    def closeNodeConnection(self):
        print(f"bye bye! from host {self.host}:)")
        self.node.close()