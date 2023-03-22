#!/usr/bin/env python3
import os
import platform

# read method 1:
# ip_file = open("files/ips.txt", "r")
# for line in ip_file:
#     if line.startswith("140."):
#         print(line)
# ip_file.close()

# read method 2:
# with open("files/ips.txt", "r") as ip_file:
#     print(ip_file.read())

# ping method 1:
def ping_host(ip):
    # Determine the currrent OS
    currrent_os = platform.system().lower()
    if currrent_os == "windows":
        # Build our ping command for Windows
        ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
    else:
        # Build our ping command for other OSs
        ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
        # Execute command and capture exit code
    exit_code = os.system(ping_cmd)
    return exit_code

def import_addresses():
    lines = []
    f = open("files/ips.txt", "r")
    for line in f:
        # Use strip() to remove spaces and carriage returns
        line = line.strip()
        # Add the line to the lines list object
        lines.append(line)
    return lines
ip_addresses = import_addresses()

for ip in ip_addresses:    
    exit_code = ping_host(ip)

    if exit_code == 0:
        print("{0} is online".format(ip))
    else:
        print("{0} is not online".format(ip))
