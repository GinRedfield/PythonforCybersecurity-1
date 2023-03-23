#!/usr/bin/env python3
import os
import platform
from datetime import datetime
import os.path

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

def write_log(message):     
    now = str(datetime.now()) + "\t"
    message = now + str(message) + "\n"
    # check is file exist, if not create a file
    if os.path.isfile("files/pinger.log"):
        f = open("files/pinger.log", "a")
        f.write(message)
    else:
        f = open("files/pinger.log", "w+")
        f.write(message)
    f.close()

def ping_host(ip):
    currrent_os = platform.system().lower()
    if currrent_os == "windows":
        ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
    else:
        ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
    exit_code = os.system(ping_cmd)
    return exit_code

def import_addresses():
    lines = []
    if os.path.isfile("files/ips.txt"):
        f = open("files/ips.txt", "r")
    for line in f:
        # Use strip() to remove WHITESPACE and carriage returns
        line = line.strip()
        lines.append(line)
    return lines

write_log("Reading IPs from ips.txt")
ip_addresses = import_addresses()
write_log("Imported {0} IPs".format(len(ip_addresses)))

for ip in ip_addresses:    
    exit_code = ping_host(ip)

    if exit_code == 0:
        write_log("{0} is online".format(ip))
    else:
        write_log("{0} is offline".format(ip))
print("done")

# write method 1:
# test_file = open("files/testfile.txt", "w")
# test_file.write("Hello World\n")
# test_file.write("I like rubber ducks\n")
# test_file.close()
