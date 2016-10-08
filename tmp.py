from scapy.all import *
p=rdpcap('filter.pcap')
a=str(p[0][3])
a.split('charset=utf-8\r\n\r\n',1)[1]

b=str(p[1][3])
b.split('charset=UTF-8\r\n\r\n',1)[1]


