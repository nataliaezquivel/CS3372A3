#! /usr/bin/env python3

import sys


def main():
    # Ask for IPv4 address in decimal form (i.e. 192.168.1.124)
    ipv4addr = input("Please enter IPv4 address in decimal form: ")
    # Ask for mask bits between 1 - 32 inclusive
    maskBit = input("Please enter a mask bit between 1 - 32: ")   
    maskBit = int(maskBit)
    # Make sure no numbers greater than 32 or less than 1 are entered
    while (maskBit < 1 or maskBit > 32):
        maskBit = input("Please enter a mask bit between 1 - 32: ")
        maskBit = int(maskBit)
    # Find matching subnet mask and number of IP addresses
    subnet, ips = mask(maskBit)
    # Find Broadcast Address
    broadAddr = submask(ipv4addr, subnet)
    # Print Results
    print("Network ID: ", ipv4addr)
    print("Broadcast Address: ", broadAddr)
    print("Subnet mask: ", subnet)
    print("Maximum number of hosts allowed in network: ", ips)

    # End of program
    sys.exit()
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
def mask(maskBit):
    if (maskBit == 1): 
        subnet = '128.0.0.0'
        ips = 2147483648
    elif (maskBit == 2): 
        subnet = '192.0.0.0'
        ips = 1073741824
    elif (maskBit == 3): 
        subnet = '224.0.0.0'
        ips = 536870912
    elif (maskBit == 4): 
        subnet = '240.0.0.0'
        ips = 268435456
    elif (maskBit == 5):
        subnet = '248.0.0.0'
        ips = 134217728
    elif (maskBit == 6):
        subnet = '252.0.0.0'
        ips = 67108864
    elif (maskBit == 7):
        subnet = '254.0.0.0'
        ips = 33554432
    elif (maskBit == 8):
        subnet = '255.0.0.0'
        ips = 16777216
    elif (maskBit == 9):
        subnet = '255.128.0.0'
        ips = 8388608
    elif (maskBit == 10):
        subnet = '255.192.0.0'
        ips = 4194304
    elif (maskBit == 11):
        subnet = '255.224.0.0'
        ips = 2097152
    elif (maskBit == 12):
        subnet = '255.240.0.0'
        ips = 1048576
    elif (maskBit == 13):
        subnet = '255.248.0.0'
        ips = 524288
    elif (maskBit == 14):
        subnet = '255.252.0.0'
        ips = 262144
    elif (maskBit == 15):
        subnet = '255.254.0.0'
        ips = 131072
    elif (maskBit == 16):
        subnet = '255.255.0.0'
        ips = 65536
    elif (maskBit == 17):
        subnet = '255.255.128.0'
        ips = 32768
    elif (maskBit == 18):
        subnet = '255.255.192.0'
        ips = 16384
    elif (maskBit == 19):
        subnet = '255.255.224.0'
        ips = 8192
    elif (maskBit == 20):
        subnet = '255.255.240.0'
        ips = 4096
    elif (maskBit == 21):
        subnet = '255.255.248.0'
        ips = 2048
    elif (maskBit == 22):
        subnet = '255.255.252.0'
        ips = 1024
    elif (maskBit == 23):
        subnet = '255.255.254.0'
        ips = 512
    elif (maskBit == 24):
        subnet = '255.255.255.0'
        ips = 256
    elif (maskBit == 25):
        subnet = '255.255.255.128'
        ips = 128
    elif (maskBit == 26):
        subnet = '255.255.255.192'
        ips = 64
    elif (maskBit == 27):
        subnet = '255.255.255.224'
        ips = 32
    elif (maskBit == 28):
        subnet = '255.255.255.240'
        ips = 16
    elif (maskBit == 29):
        subnet = '255.255.255.248'
        ips = 8
    elif (maskBit == 30):
        subnet = '255.255.255.252'
        ips = 4
    elif (maskBit == 31):
        subnet = '255.255.255.254'
        ips = 2
    elif (maskBit == 32):
        subnet = '255.255.255.255'
        ips = 1

    return (subnet, ips)
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
def submask(ipv4addr, subnet):
    ipv4addr = ipv4addr.split('.')
    subnet = subnet.split('.')
    #print(ipv4addr)
    #print(subnet) 
    ipv4addr = [int(bin(int(octet)), 2) for octet in ipv4addr]
    #print(ipv4addr)
    subnet = [int(bin(int(octet)), 2) for octet in subnet]
    #print(subnet)
    submask = [str(int(bin(ioctet & moctet), 2)) for ioctet, moctet in zip(ipv4addr, subnet)]
    #print(submask)
    host = [str(int(bin(ioctet & ~moctet), 2)) for ioctet, moctet in zip(ipv4addr, subnet)]
    #print(host)
    broadcast = [(ioctet | ~moctet) & 0xff for ioctet, moctet in zip(ipv4addr, subnet)]
    
    broadSTR = [str(int) for i in broadcast]
    broadAddr = '.'.join(broadSTR)

    return broadcast
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

if __name__ == "__main__":
    main()
