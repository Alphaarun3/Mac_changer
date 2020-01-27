#!/usr/bin/env python
import subprocess                           #comand run on os
import optparse                             #comand line arguments


def change_mac(interface, New_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", New_mac])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig"])

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface need to change its mac address")
parser.add_option("-m", "--mac", dest="New_mac", help="New mac address to change")
(options, arguments) = parser.parse_args()

