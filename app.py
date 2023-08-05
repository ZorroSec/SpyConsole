import socket 
import sys
import subprocess
import platform
import os
from colorama import Fore, Style
from datetime import datetime
from linux import linux
from windows import windows
from commands import Commands
from ascii import *
from clear import clear

name = input(f"{blue}[*]{green} Username: {reset}")
password = input(f"{blue}[*]{green} Password: {reset}")
line = '-' * 56
commandss = Commands(name, password, blue, red, green, black, cyan, line)

while True:
    try:
        opc = commandss.menu()
        inp = int(input(f"{red}/ {blue}==> {white}"))

    except Exception as e:
        print(f"\n{red}[i] {black}Error {e}")
        exit()