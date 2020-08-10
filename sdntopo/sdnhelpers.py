"""
    author: zerobits01
    purpose: writing some general purpose functions for filtering
        and checking here
    created: 10-Aug-2020
    modified: 10-Aug-2020
"""

import re


def checkIPAddress(ip):
    '''
        enter the ip as string
        return True if valid else False
    '''
    try:
        pat = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        if pat.match(ip):
            lst = ip.split('.')
            for p in lst:
                p = int(p)
                if p > 255 or p < 0:
                    print("[-] ip is not valid")
                    return False
            return True
        else:
            print("[-] ip is not valid")
            return False
    except Exception as e:
        print(e)
        return False

def checkPort(port):
    try:
        port = int(port)
        if port > 65535 or port < 0:
            print('[-] port is not valid')
            return False
        return True
    except Exception as e:
        print(e)
        return False
