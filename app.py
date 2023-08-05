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


while True:
    try:
        if platform.system() == windows():
            subprocess.call('cls', shell=True)
        else:
            subprocess.call('clear', shell=True)


        line = '-' * 56
        name = input(f"{blue}[*]{green} Username: {reset}")
        password = input(f"{blue}[*]{green} Password: {reset}")
        commandss = Commands(name, password, blue, red, green, black, cyan, line)
        commandss.gerar_cnpj()
        commandss.gerar_cpf()
        commandss.gerar_senha()
        commandss.voltar_menu()
    except Exception as e:
        print(f"\n{red}[i] {black}Error {e}")
        exit()