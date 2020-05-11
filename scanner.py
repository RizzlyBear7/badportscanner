#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 scanner.py <ip or hostname>")
#add a pretty banner
print('-' * 50)
print("Scanning target " + target)
print("Time Started " + str(datetime.now()))
print('-' * 50)

try:
    for port in range(1,65535):
        #Initalize socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Set length of connection attempt - default 1 sec
        socket.setdefaulttimeout(1)
        #returns error indicator
        result = s.connect_ex((target, port)) 
        #If port is open, print it to stdout
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

#Catch block - keyboard interrupt
except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit()

#Exception - could not be resolve hostname
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

#Exception - could not connect to given IP
except socket.error:
    print("Couldn't connect to server")
    sys.exit()