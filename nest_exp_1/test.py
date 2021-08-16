from nest.experiment import *
from nest.topology import *


red = Node('red')
blue = Node('blue')

(eth0,eth1) = connect(red,blue)

eth0.set_address('10.0.0.1/24')
eth1.set_address('10.0.0.2/24')

red.ping(eth1.address)

eth0.set_attributes('5mbit','5ms')
eth1.set_attributes('10mbit','10ms')

flow = Flow(red,blue,eth1.address,0,10,2)

exp = Experiment('tcp_2up')
exp.add_tcp_flow(flow,'reno')
exp.run()
