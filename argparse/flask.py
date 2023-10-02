# -*- coding: UTF-8 -*-

import argparse
from scapy.all import *


#打印端口状态
def print_ports(port, state):
    print("%s | %s" % (port, state))

def tcpScan(target,ports):
    pass
def synScan(target,ports):
    pass
def ackScan(target,ports):
    pass
def windowScan(target,ports):
    pass
def nullScan(target,ports):
    pass
def finScan(target,ports):
    pass
def xmaxScan(target,ports):
    pass

def udpScan(target,ports):
    pass


if __name__ == '__main__':

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
    if scantype == "T":#全连接扫描
        pass
    elif scantype == "S":#syn扫描
        pass
    elif scantype == "A":#ack扫描
        pass
    elif scantype == "W":#TCPwindow扫描
        pass
    elif scantype == "N":#NULL扫描
        pass
    elif scantype == "F":#FIN扫描
        pass
    elif scantype == "X":#Xmas扫描
        pass
    elif scantype == "U":#UDP扫描
        pass
    else:
        print("不支持当前模式")
