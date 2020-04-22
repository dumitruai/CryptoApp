#!/usr/bin/env python3

from os import remove
from os.path import splitext

from re import findall
from random import choice, randint

#from pyAesCrypt import encryptFile, decryptFile
#rom rsa import newkeys, encrypt, PublicKey, decrypt, PrivateKey

def getNumbers(text):
    template = r"[0-9]+"
    return findall(template, text)

def getTwoSymbols(text):
    template = r"[A-Z]{2}"
    return findall(template, text)

### Caesar ###
def caesar(mode, message, key):
	message=list(message.upper())
	try: key = int(key)
	except: return "KEY is not INT type";

	for index, symbol in enumerate(message):
   		if mode == 'E':
   			message[index] = chr((ord(symbol) + key - 13)%26 + ord('A'))
   		else:
   			message[index] = chr((ord(symbol) - key - 13)%26 + ord('A'))
	return "".join(message)
### Caesar ###