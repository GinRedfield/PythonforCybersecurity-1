#!/usr/bin/env python3
import platform
import os
import subprocess
import re
import netifaces as ni

# method 1:
# os.system("ping -c 1 -w 2 8.8.8.8")

# method 2:
# ip = "127.0.0.1"
# ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
# exit_code = os.system(ping_cmd)
# print(exit_code)

# method 3:
# ifconfig |  grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" | head -n 1 | grep -Po ".*(?=\.)"
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

ip_prefix = ni.ifaddresses('enp0s3')[ni.AF_INET][0]['addr']
ip_prefix = re.sub(r"\.[^.]+$", "",ip_prefix) + "."


for final_octet in range(254):
    ip = ip_prefix + str(final_octet + 1)
    exit_code = ping_host(ip)

    if exit_code == 0:
        print("{0} is online".format(ip))



