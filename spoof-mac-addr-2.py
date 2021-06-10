#!/usr/bin/python3
'''Spoof MAC address. (as a cybersecurity enhancement)'''
from random import randint
from random import choice
from subprocess import run

# pseudo-randomly generated MAC address
mac_addr = f"{hex(choice(range(16, 255, 2)))[2:]}:{hex(randint(16, 256))[2:]}:\
{hex(randint(16, 256))[2:]}:{hex(randint(16, 256))[2:]}:\
{hex(randint(16, 256))[2:]}:{hex(randint(16, 256))[2:]}"

print(mac_addr)
run(["sudo", "ip", "link", "set", "enp2s0", "address", mac_addr], check=True)

