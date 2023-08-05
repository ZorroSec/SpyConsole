from colorama import Fore, Style
import os
import time


blue = Fore.LIGHTBLUE_EX
red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
black = Fore.LIGHTBLACK_EX
reset = Style.RESET_ALL
cyan = Fore.LIGHTCYAN_EX
white = Fore.LIGHTWHITE_EX

class Ascii:
	def clear():
		os.system('cls||clear')

	def temp():
		time.sleep(0.225)