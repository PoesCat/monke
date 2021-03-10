from random import randint
import time
import threading
import os
import ctypes
import sys

mymonkoins = 0
addedmonkoins = 0


def getmonkoinvalue():
	monke = randint(1,69)
	return round((69/14*21 - monke * 1.05), 2)



def printmonkoinprice():
	global addedmonkoins
	global mymonkoins
	while True:
		ctypes.windll.kernel32.SetConsoleTitleW('Current monkoin price > 1 monkoin = $' + str(getmonkoinvalue()) + '   |   Monkoins to $$$ > $' + str(round(mymonkoins * getmonkoinvalue(), 2)))
		time.sleep(1)


def mine():
	global mymonkoins
	global addedmonkoins
	while True:
		os.system('cls')
		addedmonkoins += randint(1,11)
		mymonkoins += addedmonkoins
		print('Mined ' +  str(addedmonkoins)  + ' monkoins.\nCurrent monkoins > ' + str(mymonkoins))
		addedmonkoins = 0
		print()
		sys.stdout.write('\rMining monkoins /')
		sys.stdout.flush()
		time.sleep(0.1)
		sys.stdout.write('\rMining monkoins -')
		sys.stdout.flush()
		time.sleep(0.1)
		sys.stdout.write('\rMining monkoins \\')
		sys.stdout.flush()
		time.sleep(0.1)
		sys.stdout.write('\rMining monkoins |')
		sys.stdout.flush()
		time.sleep(0.1)
		sys.stdout.write('\rMining monkoins /')
		sys.stdout.flush()
		time.sleep(0.1)
		sys.stdout.write('\rMining monkoins -')
		sys.stdout.flush()
		time.sleep(0.1)
		sys.stdout.write('\rMining monkoins \\')
		time.sleep(0.1)
		sys.stdout.write('\rMining monkoins |')
		time.sleep(0.1)
	

input('Welcome monke!\nPress enter to starting mining monkoins!')

threading.Thread(target=printmonkoinprice).start()
mine()