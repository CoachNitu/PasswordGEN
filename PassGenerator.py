#
# ==========================================+date : 2020/5/28+===============================================

import sys
import os
import time
import subprocess

import platform

import pyperclip as pyperclip


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)


slowprint("[!] Starting : ")
time.sleep(2)
os.system('')


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)


slowprint("    \033[91m")
print('''                              


.########.....###.....######...######..##......##..#######..########..########....
.##.....##...##.##...##....##.##....##.##..##..##.##.....##.##.....##.##.....##...
.##.....##..##...##..##.......##.......##..##..##.##.....##.##.....##.##.....##...
.########..##.....##..######...######..##..##..##.##.....##.########..##.....##...
.##........#########.......##.......##.##..##..##.##.....##.##...##...##.....##...
.##........##.....##.##....##.##....##.##..##..##.##.....##.##....##..##.....##...
.##........##.....##..######...######...###..###...#######..##.....##.########....



..######...########.##....##.########.########.....###....########..#######..########.
.##....##..##.......###...##.##.......##.....##...##.##......##....##.....##.##.....##
.##........##.......####..##.##.......##.....##..##...##.....##....##.....##.##.....##
.##...####.######...##.##.##.######...########..##.....##....##....##.....##.########.
.##....##..##.......##..####.##.......##...##...#########....##....##.....##.##...##..
.##....##..##.......##...###.##.......##....##..##.....##....##....##.....##.##....##.
..######...########.##....##.########.##.....##.##.....##....##.....#######..##.....##


                                                                                         ''')


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0. / 100)


slowprint('''\033[1;31m \033[91m ''')


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)


slowprint("\t\t                                                   \033[93mBy :Nitu")

import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+}{"
length = int(input("Enter password length ==> "))
print('')
slowprint("Generating Password please wait")
print('')
password = ""
for i in range(length):
    password += random.choice(chars)
time.sleep(2)
os.system('')
print(password)
print('')
time.sleep(0.9)
os.system('')
print("[!]Password Copied to Clipboard")
pyperclip.copy(password)
print('')
