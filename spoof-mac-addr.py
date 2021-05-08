#!/usr/bin/python3
'''Spoof MAC address. (as a cybersecurity enhancement)'''
from csv import reader
from random import randint as ri
from subprocess import run


with open('csv/oui.csv') as csv_file:
    csv_reader = reader(csv_file)
    oui_list = []
    for rec in csv_reader:
        oui_list.append(rec[0])
    oui_h = oui_list[ri(0, len(oui_list))]
    oui = ':'.join(oui_h.split('-'))

mac_rgt = f"{hex(ri(16, 256))[2:]}:{hex(ri(16, 256))[2:]}:{hex(ri(16, 256))[2:]}"

print(f"{oui}:{mac_rgt}")

run(["sudo", "ip", "link", "set", "enp2s0", "address", f"{oui}:{mac_rgt}"], check=True)
