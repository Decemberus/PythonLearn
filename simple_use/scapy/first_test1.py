import sys
from scapy.all import *
from scapy.layers.inet import IP, ICMP

p=sr1(IP(dst='192.168.1.1')/ICMP())
if p:
    p.show()