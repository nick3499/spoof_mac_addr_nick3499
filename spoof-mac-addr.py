#!/usr/bin/python3
'''Spoof MAC address. (as a cybersecurity enhancement)'''
from csv import reader
from random import randrange as rr
from subprocess import run


with open('csv/oui.csv') as csv_f:
    csv_r = reader(csv_f)
    oui_l = []
    for rec in csv_r:
        oui_l.append(rec[0])
    oui_h = oui_l[rr(0, len(oui_l))]
    oui = ':'.join(oui_h.split('-'))

mac_rgt = f"{hex(rr(16, 256))[2:]}:{hex(rr(16, 256))[2:]}:{hex(rr(16, 256))[2:]}"

run(["sudo", "ip", "link", "set", "enp2s0", "address", f"{oui}:{mac_rgt}"], check=True)

