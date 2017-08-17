#!/usr/bin/python3

from platform import system as system_name
from os import system as system_call

#List of domain names or IPs that you want to check, in quotes, separated by commas
servers = [ "google.com", "facebook.com", "yahoo.com", "8.8.8.8" ] 

def ping(host):
    return system_call("ping -c 1 " + host + " > /dev/null 2>/dev/null") == 0
    
allgreen = 1

messages = []

for i in servers:  #First we'll check to see if all the servers are reachable
    if ping(i) == True: #If a server is reachable get the ping time
        system_call("ping -c 1 " + i + " | awk 'BEGIN {FS=\"[=]|[ ]\"} {print$10}' > tmp.tmp")
        f = open('tmp.tmp')		#Dirty but easy method of cleanly extracting ping time
        lines = f.readlines()
        lat = lines[1] 
        lat = "".join(lat.split())
        messages.append(i + " is up and reachable (" + lat + "ms)")
        
    else: #If a server is not reachable
        messages.append("\033[1;31m" + i + " is not reachable.\033[0m")
        allgreen = 0
        
if allgreen == 1:
    print("\033[1;32m•\033[0m")   #If all the servers are reachable output a subtle green light
else:
    print("\033[1;31m!\033[0m")   #If a server is not reachable then output a scary red exclamation mark

print("---")

if allgreen == 1:
    print("\033[1;32mAll Servers Up and Reachable!\033[0m")
else:
    print("\033[1;31mOne or More Servers Not Reachable!\033[0m")

for i in messages:
    print(i)
