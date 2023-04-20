#!/usr/bin/env python3
import argparse
import sys
import socket
import random
import struct
import time

from scapy.all import sendp, send, get_if_list, get_if_hwaddr
from scapy.all import Packet
from scapy.all import Ether, IP, UDP, TCP, RTP
sent_pkt_infos = []
def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print("Cannot find eth0 interface")
        exit(1)
    return iface

def main():

    if len(sys.argv)<2:
        print('pass 1 argument: <destination>')
        exit(1)

    addr = socket.gethostbyname(sys.argv[1])
    iface = get_if()

    print(("sending on interface %s to %s" % (iface, str(addr))))
    pkt =  Ether(src='00:00:00:00:00:00', dst='ff:ff:ff:ff:ff:ff')
    pkt = pkt /IP(dst=addr) / TCP(dport=1234, sport=random.randint(49152,65535), seq=897,ack=897,flags="A")
    sent_pkt_infos.append({
        "timestamp"      : time.time()
    })
    pkt.show2()
    
    sendp(pkt, iface=iface, verbose=False)


if __name__ == '__main__':
    main()
