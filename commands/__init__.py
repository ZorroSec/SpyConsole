import socket 
import sys
import subprocess
import platform
import os
from colorama import Fore, Style
from datetime import datetime
from linux import linux
from windows import windows
from requests import get
from requests import post
from json import loads
from random import randint
from ascii import *
from random import choice
import string
from clear import clear
from banner import banner


class Commands:
	def __init__(self, blue, red, green, black, cyan, white):
		self.blue = blue
		self.red = red
		self.green = green
		self.black = black
		self.cyan = cyan
		self.white = white
	
	def menu(self):
		clear()
		func = {
			'Consultas':['CEP', 'CNPJ'],
	  		'Tools':['Gerar CPF', 'Gerar CNPJ', 'Gerar SENHA']
		}

		print(banner())
		print(line)
		for c, key in enumerate(func.keys()):
			print(f"{self.blue:^28}[{self.green}{c+1}{self.blue}] {self.white}{key:^28}")
		print(line)
		opc = input(f"{self.blue} ==> {self.white}").replace("0", "")
		clear()
		print(banner())
		if opc == "1":
			for c, item in enumerate(func['Consultas']):
				print(f"{self.blue:^28}[{self.cyan}0{c+1}{self.blue}] {self.white}{item:^10}")
			print(line)
		elif opc == "2":
			for c, item in enumerate(func['Tools']):
				print(f"{self.blue:^28}[{self.cyan}0{c+1}{self.blue}] {self.white}{item:^10}")
			print(line)
		else:
			print(f"{self.red}Comando Invalido!")
			Commands.menu()
		return opc
		
	def voltar_menu(self):
		try:
			voltar = input(f"{black}[{blue}i{black}] {red}Enter Para Voltar ao menu{Style.RESET_ALL}")
		except KeyboardInterrupt:
			print(f"{red}You typed ctrl + C")

	def gerar_cpf(self):
		cpf = [randint(0, 9) for x in range(9)]
		for _ in range(2):
			val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11

			cpf.append(11 - val if val > 1 else 0 )
		print("%s%s%s.%s%s%s.%s%s%s-%s%s"%tuple(cpf))
	def gerar_cnpj(self):
		def calculate_special_digit(l):
			digit = 0
			for i, v in enumerate(l):
				digit += v * (i % 8 + 2)
			
			digit = 11 - digit % 11

			return digit if digit < 10 else 0
		cnpj = [1,0,0,0] + [randint(0, 9) for x in range(8)]

		for _ in range(2):
			cnpj = [calculate_special_digit(cnpj)] + cnpj
		
		print("%s%s%s.%s%s%s.%s%s%s/%s%s%s-%s%s"%tuple(cnpj[::-1]))
	def gerar_senha(self):
		size = int(input(f"{blue}[*] {green}Numero De Digitos: {Style.RESET_ALL}"))
		caracteres = string.ascii_letters + string.digits + string.punctuation
		senha = ""

		for i in range(size):
			senha += choice(caracteres)
		print(senha)
	def pscanner():
		if platform.system() == windows():
			subprocess.call('cls', shell=True)
		else:
			subprocess.call('clear', shell=True)

		remoteServer = input(f"{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTGREEN_EX}Hostname: {Fore.BLACK}")
		remoteServerIp = socket.gethostbyname(str(remoteServer))

		t1 = datetime.now()

		print("-" * 60)
		print(f"{Fore.LIGHTBLACK_EX}escaneando o Host remoto com IP ~{Fore.GREEN}{remoteServerIp}{Fore.LIGHTBLACK_EX}~ ")
		print(f"-" * 60)
		try:
			for porta in range(0, 1025):
				#print(porta)
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.settimeout(0.025)
				resultado = sock.connect_ex((remoteServerIp, porta))
				if resultado == "0":
					print(f"{Style.RESET_ALL}{porta} {Fore.LIGHTGREEN_EX}[ABERTA]")
				sock.close()
		except KeyboardInterrupt:
			print("\nVocê pressionou Ctrl+C")
			sys.exit()
		except socket.gaierror:
			print('\nO hostname não pode ser resolvido. Saindo!')
			sys.exit()
		except socket.error:
			print("\nNão foi possível realizar a conexão com o servidor!")
			sys.exit()

		t2 = datetime.now()
		
		total =  t2 - t1
		
		print('\nEscaner completo em ', total)