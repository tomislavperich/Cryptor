#! /usr/bin/env python
import os
import time
import math
import sys
import getpass

# Name: Cryptor
# Version: 0.1
# Author: Tomislav Peric
# Date: 5th of June 2015

def encrypt():
	
	# What do we want to do?
	# -Convert message to ASCII num - Done
	# -Convert key to ASCII num - Done
	# -Get a total of keys (ex. "114 + 115 + 116") - Done
	# -Increment total by 500 so ugly characters
	# could be avoided - Done
	# -Take last two numbers of key total - Done
	# -Subtract each element in message by the 
	# total of keys - Done
	# -Convert message back to text (chr) and print it. - Done
	
	os.system('clear')
	rawinput = input("String to encrypt: ")
	enckey = getpass.getpass("Enter a key: ")
	oldkey = enckey
	
	toencrypt = []
	encrypted = []
	tochar = []
	enckeysplit = []
	enckeyord = []
	encmath = 0
	for i in enckey:
		enckeysplit.append(i)
	
	for i in enckeysplit:
		enckeyord.append(ord(i))
	
	for i in enckeyord:
		encmath += i

	encmath = round(math.sqrt(encmath))
	encmath = encmath - 5
	encmath = int(encmath)

	for i in rawinput:
		toencrypt.append(i)
	
	for i in toencrypt:
		encrypted.append(ord(i) - encmath)
	
	for i in encrypted:
		tochar.append(str(chr(i)))
	
	enckeyf = ''.join(tochar)
	
	os.system('clear')
	print("Encrypted string: " + enckeyf)
	print()
	input("Press Enter to go back to main menu...")
	choice()

def decrypt():
	
	# What do we want to do?
	# -Same shit but somewhat backwards
	
	os.system('clear')
	rawinput = input("String to decrypt: ")
	enckey = getpass.getpass("Enter a key: ")
	
	todecrypt = []
	enckeysplit = []
	enckeyord = []
	enckeyf = ""
	decrypted = []
	tochar = []
	encmath = 0
	
	for i in rawinput:
		todecrypt.append(ord(i))
	
	for i in enckey:
		enckeysplit.append(i)
	
	for i in enckeysplit:
		enckeyord.append(ord(i))
	
	for i in enckeyord:
		encmath += i
	
	encmath = round(math.sqrt(encmath))
	encmath = encmath - 5
	encmath = int(encmath)
	
	for i in todecrypt:
		decrypted.append(i + encmath)

	for i in decrypted:
		tochar.append(chr(i))

	enckeyf = "".join(tochar)

	os.system('clear')
	print("Decrypted data: " + enckeyf)
	print()
	input("Press Enter to go back to main menu...")
	choice()
	
def about():
	os.system('clear')
	print("This script was made by Tomislav Peric.\n\nSpecial thanks to:\n-Milan Lacok\n-Milan Nestorovic\n-Luka Dimitrijevic")
	print()
	print("Cryptor v0.1 - 4.6.2015.")
	print()
	input("Press Enter to continue...")
	choice()
	
def exit():
	os.system('clear')
	print("Bye!")
	time.sleep(.5)
	os.system('clear')
	sys.exit(0)

def choice():
	os.system('clear')
	print("Encrypt or decrypt?\n1. Encrypt\n2. Decrypt\n3. About\n4. Exit")
	q1 = input("Make a choice (1, 2, 3, 4): ")

	if q1 == "1":
		
		encrypt()
	elif q1 == "2":
		
		decrypt()
	elif q1 == "3":
		about()
	elif q1 == "4":
		exit()
	else:
		os.system('clear')
		print("Unknown command, please try again!")
		time.sleep(1)
		
		choice()

choice()

