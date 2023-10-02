# -*- coding: UTF-8 -*-

import argparse
from scapy.all import *
from scapy.layers.inet import IP, TCP, ICMP, UDP


# 打印端口状态
def print_ports(port, state):
    print("%s | %s" % (port, state))


def tcpScan(target, ports):
    for i in ports:
        package = sr1(IP(src=target) / TCP(dport = i,flags = "S"))  # 这一行其实会自动发送包
        if package is None:
            print("uable to create package")
        elif package.haslayer("TCP"):
            print(package["TCP"].flags)
            if send["TCP"].flags =="SA":
                package_back = sr1(IP(src = target) / TCP(dport = i, flags = "RA"))
                print(f"the port {i} is open")
            elif send["TCP"].flags == "RA": #应该是收到了原来的包
                print(f"the port is closing")
def synScan(target, ports):
    for i in ports:
        package = sr1(IP(src=target) / TCP(dport = i,flags = "S"))  # 这一行其实会自动发送包
        if package is None:
            print("uable to create package")
        elif package.haslayer("TCP"):
            print(package["TCP"].flags)
            if send["TCP"].flags =="SA":
                package_back = sr1(IP(src = target) / TCP(dport = i, flags = "R"))
                print(f"the port {i} is open")
            elif send["TCP"].flags == "RA": #应该是收到了原来的包
                print(f"the port is closing")


def ackScan(target,ports):
    print("tcp ack扫描 %s with ports %s" % (target, ports))
    for port in ports:
        ack_flag_scan_resp = sr1(IP(dst=target)/TCP(dport=port,flags="A"),timeout=5)
        print(str(type(ack_flag_scan_resp)))
        #当没有数据的时候debug出现的形式是<class 'NoneType'>，所以出现了Nonetype就是无数据返回
        if (str(type(ack_flag_scan_resp))=="<class 'NoneType'>"):
            print_ports(port,"filtered")
        elif(ack_flag_scan_resp.haslayer(TCP)):
            if(ack_flag_scan_resp["TCP"].flags == "R"):
                print_ports(port,"unfiltered")
        elif(ack_flag_scan_resp.haslayer(ICMP)):
            if(int(ack_flag_scan_resp["ICMP"].type)==3 and int(ack_flag_scan_resp["ICMP"].code) in [1,2,3,9,10,13]):
                print_ports(port,"filtered")
        else:
            print_ports(port,"filtered")
def windowScan(target, ports):
    print("tcp window扫描 %s with ports %s" % (target, ports))
    for port in ports:
        ack_flag_scan_resp = sr1(IP(dst=target)/TCP(dport=port,flags="A"),timeout=5)
        print(str(type(ack_flag_scan_resp)))
        if str(type(ack_flag_scan_resp)) == "<class 'NoneType'>":
            print(f"{port} filtered")
        elif(ack_flag_scan_resp.haslayer(TCP)):
            if ack_flag_scan_resp["TCP"].window == 0:
                print(f"{port} closed")
            elif ack_flag_scan_resp["TCP"].window != 0:
                print(f"{port} open")

def nullScan(target, ports):
    print("tcp window扫描 %s with ports %s" % (target, ports))
    for port in ports:
        ack_flag_scan_resp = sr1(IP(dst=target)/TCP(dport=port,flags="A"),timeout=5)
        print(str(type(ack_flag_scan_resp)))
        if str(type(ack_flag_scan_resp)) == "<class 'NoneType'>":
            print(f"{port} filtered")
        elif(ack_flag_scan_resp.haslayer(TCP)):
            if ack_flag_scan_resp["TCP"].flags == "R" or "RA" :
                print(f"{port} closed")
        elif ack_flag_scan_resp.haslayer(ICMP):
            if ack_flag_scan_resp["ICMP"].type == 3 and int(ack_flag_scan_resp["ICMP"].code) in [1,2,3,9,10,13]:
                print(f"{port} filter")


def finScan(target,ports):
    print("tcp FIN 扫描 %s with ports %s" % (target, ports))
    for port in ports:
        fin_scan_resp = sr1(IP(dst=target)/TCP(dport=port,flags="F"),timeout=5)
        if (str(type(fin_scan_resp))=="<class 'NoneType'>"):
            print_ports(port, "Open|Filtered")
        elif(fin_scan_resp.haslayer(TCP)):
            #RST和ACK被置为1
            if(fin_scan_resp.getlayer(TCP).flags == 0x14):
                print_ports(port, "Closed")
        elif(fin_scan_resp.haslayer(ICMP)):
            if(int(fin_scan_resp.getlayer(ICMP).type)==3 and int(fin_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                print_ports(port, "Filtered")


def xmaxScan(target, ports):
    print("tcp Xmax 扫描 %s with ports %s" % (target, ports))
    for port in ports:
        fin_scan_resp = sr1(IP(dst=target) / TCP(dport=port, flags="PFU"), timeout=5)
        if (str(type(fin_scan_resp)) == "<class 'NoneType'>"):
            print_ports(port, "Open")
        elif (fin_scan_resp.haslayer(TCP)):
            # RST和ACK为1
            if (fin_scan_resp.getlayer(TCP).flags == 0x14):
                print_ports(port, "Closed")
        elif (fin_scan_resp.haslayer(ICMP)):
            if (int(fin_scan_resp.getlayer(ICMP).type) == 3 and int(fin_scan_resp.getlayer(ICMP).code) in [1, 2, 3, 9,10, 13]):
                print_ports(port, "Filtered")


def udpScan(target,ports):
    print("UDP 扫描 %s with ports %s" % (target, ports))
    for port in ports:
        udp_scan_resp = sr1(IP(dst=target)/UDP(dport=port),timeout=5)
        if (str(type(udp_scan_resp))=="<class 'NoneType'>"):
            print_ports(port, "Open|Filtered")
        elif(udp_scan_resp.haslayer(UDP)):
            if(udp_scan_resp.getlayer(TCP).flags == "R"):
                print_ports(port, "Open")
        elif(udp_scan_resp.haslayer(ICMP)):
            if(int(udp_scan_resp.getlayer(ICMP).type)==3 and int(udp_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                print_ports(port, "Filtered")


if __name__ == '__main__':
    # ports = range(1, 65535)
    # ports = range(80, 81)
    # ackScan("127.0.0.1",ports)

    parser = argparse.ArgumentParser("")
    parser.add_argument("-t", "--target", help="目标IP", required=True)
    parser.add_argument("-p", "--ports", type=int, nargs="+", help="指定端口列表 (21 23 80 ...)")
    parser.add_argument("-s", "--scantype", help="""
    "T":全连接扫描
    "S":syn扫描
    "A":ack扫描
    "W":TCPwindow扫描
    "N":NULL扫描
    "F":FIN扫描
    "X":Xmas扫描
    "U":UDP扫描
    """, required=True)
    args = parser.parse_args()

    target = args.target
    scantype = args.scantype
    if args.ports:
        ports = args.ports
    else:
        ports = range(1, 65535)

    # 扫码方式
    if scantype == "T":  # 全连接扫描
        pass
    elif scantype == "S":  # syn扫描
        pass
    elif scantype == "A":  # ack扫描
        pass
    elif scantype == "W":  # TCPwindow扫描
        pass
    elif scantype == "N":  # NULL扫描
        pass
    elif scantype == "F":  # FIN扫描
        pass
    elif scantype == "X":  # Xmas扫描
        pass
    elif scantype == "U":  # UDP扫描
        pass
    else:
        print("不支持当前模式")
