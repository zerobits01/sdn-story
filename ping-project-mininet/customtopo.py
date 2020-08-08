
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )
        
        # Add hosts and switches
        leftHost0 = self.addHost( 'h0' )
        leftHost1 = self.addHost( 'h1' )
        leftHost2 = self.addHost( 'h2' )
        rightHost0 = self.addHost( 'h3' )
        rightHost1 = self.addHost( 'h4' )
        leftSwitch = self.addSwitch( 's0' )
        rightSwitch = self.addSwitch( 's1' )

        # Add links
        self.addLink( leftHost0, leftSwitch )
        self.addLink( leftHost1, leftSwitch )
        self.addLink( leftHost2, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost0 )
        self.addLink( rightSwitch, rightHost1 )


topos = { 'mytopo': ( lambda: MyTopo() ) }

# running script : > sudo mn --custom customtopo.py --topo mytopo --controller=remote,ip=172.16.141.132,port=6653 --switch=ovsk,protocols=OpenFlow13 --mac

