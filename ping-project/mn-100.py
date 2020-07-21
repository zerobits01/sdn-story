from mininet.topo import Topo


'''
    implementing linear topo with python mininet command : 
    > sudo mn --controller=remote,ip=<ip-address>,port=6653 --topology=linear,100 --switch=ovsk,protocols=OpenFlow13
'''

# for running the script : sudo mn --custom mn-100.py --topo=hundrdtopo --mac --switch=ovsk,protocols=openflow13 --link=tc --controller=remote,ip=127.0.0.1,port=6633

class MyHundredTopo( Topo ):
    def __init__(self):
        Topo.__init__(self)
        hosts = []
        switches = []


        # initializing the hosts
        for i in range(0,100,1):
            hosts.append(self.addHost('h'+i))


        # initializing the switches
        for i in range(0,100,1):
            switches.append(self.addSwitch('s'+i))


        # adding the links between the switches
        for i in range(0,100,2):
            self.addLink(switches[i], switches[i+1], bw=15)


        # adding the links between hosts and switches
        for i in range(0,100,1):
            self.addLink(switches[i], hosts[i], bw=10)
   
test = {'hundrdtopo' : lambda : MyHundredTopo() } # creating the topology
