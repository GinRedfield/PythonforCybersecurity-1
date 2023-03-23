#!/usr/bin/env python3
import nmap
import netifaces as ni
# import re

ip = ni.ifaddresses('enp0s3')[ni.AF_INET][0]['addr']
# ip = re.sub(r"\.[^.]+$", "",ip) + ".20"

port_start = 1
port_end = 100
scanner = nmap.PortScanner()
print("Scanning {0}".format(ip))

for port in range(port_start, port_end + 1):
    result = scanner.scan(ip, str(port))
    port_status = result['scan'][ip]['tcp'][port]['state']
    print("\tPort: {0} is {1}".format(port, port_status))