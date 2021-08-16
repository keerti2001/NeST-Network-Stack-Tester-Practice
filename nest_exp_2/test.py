from nest.experiment import *
from nest.topology import *


red = Node('red')
router = Node('router')
blue = Node('blue')


(eth0,eth1) = connect(red,router)
(eth2,eth3) = connect(router,blue)

eth0.set_address('10.0.0.1/24')
eth1.set_address('10.0.0.2/24')
eth2.set_address('10.0.1.1/24')
eth3.set_address('10.0.1.2/24')

red.add_route('DEFAULT' , eth0)
blue.add_route('DEFAULT' , eth3)

router.enable_ip_forwarding()

eth0.set_attributes('1gbit','5ms')
eth1.set_attributes('1gbit','5ms')
eth2.set_attributes('100mbit','10ms','codel')
eth3.set_attributes('100mbit','10ms')

flow = Flow(red,blue,eth3.address,0,20,2)
flow_udp = Flow(red,blue,eth3.address,0,20,1)

exp = Experiment('tcp+udp')
exp.add_udp_flow(flow_udp,target_bandwidth='100mbit')
exp.add_tcp_flow(flow)
exp.require_qdisc_stats(eth2)
exp.run()
