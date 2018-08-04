import socket
import textwrap
import time
from ctypes import *
import binascii
import struct

# IP header
class ip_h(Structure):

    _fields_ = [
        ("version", c_ubyte, 4),
        ("ihl", c_ubyte, 4),
        ("tos", c_ubyte),
        ("len", c_ushort),
        ("id", c_ushort),
        ("offset", c_ushort),
        ("ttl", c_ubyte),
        ("proto", c_ubyte),
        ("checksum", c_ushort),
        ("src", c_uint32),
        ("dst", c_uint32),
    ]

    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):

        self.version = 4
        self.ihl = 5
        self.vihl = self.version * self.ihl

        self.src_address = socket.inet_ntoa(struct.pack("@I", self.src))  # human readable ip address
        self.dst_address = socket.inet_ntoa(struct.pack("@I", self.dst))

        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
        try:
            self.protocol = self.protocol_map[self.proto]
        except:
            self.protocol = str(self.proto)



class eth_h(Structure):

    _fields_ = [
        ("dst_mac", c_uint16 * 3),
        ("src_mac", c_uint16 * 3),
        ("eth_proto", c_ushort),
    ]

    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):

        self.dmac = binascii.hexlify(self.dst_mac)
        self.smac = binascii.hexlify(self.src_mac)
        socket.htons(self.eth_proto)


sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))


while True:

    data = sniffer.recvfrom(65535)[0]    #read in a packet and pass first 20 bytes
    frame = eth_h(data[:14]) #frame
    ip = ip_h(data[14:])
    if frame.eth_proto == 8:
     
        start_time = time.time()
        print("Time: {},Source: {}, Destination: {}, Protocol: {}, Length: {}".format(start_time,ip.src_address, ip.dst_address,ip.protocol,ip.vihl))
    
