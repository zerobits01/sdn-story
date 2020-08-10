"""
    author: zerobits01
    purpose: config file custom lib for handling IP and default route addresses
    created: 10-Aug-2020
    modified: 10-Aug-2020
"""

import configparser

cfg = configparser.ConfigParser()


def readConfig(config_file):
    '''
        reads config file from the topo.cfg and returns the dictionary
    '''
    cfg.read(config_file)
    return cfg


def writeConfig():
    '''
        writes default config in to topo.cfg
    '''
    # ip, users, pass, ...
    cfg['controller'] = {

    }

    cfg['router'] = {

    }

    cfg['admin'] = {

    }

    cfg['employee1'] = {

    }
    cfg['employee1'] = {

    }

    cfg['server1'] = {

    }
    cfg['server2'] = {

    }
    cfg['server3'] = {

    }
    cfg['server4'] = {

    }

    cfg.write(open("topo.cfg", 'w'))


if __name__ == "__main__":
    try:
        dct = readConfig('topo.cfg')
        print(dct['server']['ip'])
    except Exception as e:
        print(e)
        with open("topo.cfg", "w") as config_file:
            writeConfig()
