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

while True:
    try:
        commandss = Commands(blue, red, green, black, cyan, white)

        opc = commandss.menu()
        inp = int(input(f"{red}/ {blue}==> {white}"))

    except KeyboardInterrupt:
        print(f"\n{red}[i] {black}Error ")
        exit()