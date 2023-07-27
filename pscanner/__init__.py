import socket 
import sys
import subprocess
import platform
import os
from datetime import datetime

def pscanner():
	if platform.system() == "Windows":
		subprocess.call('cls', shell=True)
	else:
		subprocess.call('clear', shell=True)

	remoteServer = input(f"")