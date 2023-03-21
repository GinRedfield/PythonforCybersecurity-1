#!/usr/bin/env python3
import platform
import os

# test = os.system('ping -c 1 -w 2 8.8.8.8  > /dev/null 2&>1')
# print(test)

# ip = "127.0.0.1"
# ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
# exit_code = os.system(ping_cmd)
# print(exit_code)

ip_prefix = '140.161.83.'
currrent_os = platform.system().lower()

for final_octet in range(254):
    ip = ip_prefix + str(final_octet + 1)
    if currrent_os == 'windows':
        ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
    if currrent_os == 'linux' :
        ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
    exit_code = os.system(ping_cmd)
    if exit_code == 0:
        print("{0} is online".format(ip))
# Print results to console
print(exit_code)