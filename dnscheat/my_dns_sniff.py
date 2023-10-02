from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sniff

scapy.config.conf.sniff_promisc=True #设置混杂模式
def packageHandler(pkt):
    dport = pkt[IP][TCP].dport
    if dport == 80 and pkt[IP][TCP].payload:
        print(f"already capture {pkt[IP][TCP].payload}")
if __name__ =='__main__':
    sniff(prn=packageHandler,iface='vEthernet')
