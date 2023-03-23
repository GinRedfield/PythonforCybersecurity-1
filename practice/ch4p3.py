#!/usr/bin/env python3
import netifaces as ni
# import re

ip = ni.ifaddresses('enp0s3')[ni.AF_INET][0]['addr']
# ip = re.sub(r"\.[^.]+$", "",ip) + ".20"

def toBinary(integer):
    binary = ['{0:0>8}'.format(bin(int(x))[2:]) for x in integer.split(".")]
    return binary

def ip_information(ip, mask):
    binary_ip = toBinary(ip)
    binary_mask = toBinary(mask)
    network_ip = ["", "", "", ""]
    broadcast_address = ["", "", "", ""]
    number_of_hosts = 1

    for x in range(4):
        for y in range(8):
            network_ip[x] += str(int(binary_ip[x][y]) and int(binary_mask[x][y]))
            broadcast_address[x] += str(int(not int(binary_mask[x][y])))
            if binary_mask[x][y] == '0':
                number_of_hosts *= 2

        network_ip[x] = int(network_ip[x], 2)
        broadcast_address[x] = int(broadcast_address[x], 2) + network_ip[x]

    return f"""
    Network IP: {".".join(str(x) for x in network_ip)}
    Broadcast address: {".".join(str(x) for x in broadcast_address)}
    Number of hosts: {number_of_hosts - 2}
    """

print(ip)
print(toBinary(ip))
print(ip_information(ip, "255.255.255.0"))
