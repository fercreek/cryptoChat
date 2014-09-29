#!/usr/bin/python
import string
import os
import sys
from random import choice

def keys(amount, key_len):
	(amount,key_len) = (int(amount),int(key_len)) 
	totalKeys = ""
	r = '10'
	for a in range(amount):
		kl = ""
		for k in range(key_len):
			kl += choice(r)
		totalKeys += kl + '\n'
	return totalKeys

def writing(key):
	f=open("keys/keyA.txt","w")
	f.write(key)
	f.close()
	f=open("keys/keyB.txt","w")
	f.write(key)
	f.close()

try:
	key = keys(sys.argv[1],sys.argv[2])
except: 
	print "Intenta de nuevo"	
	sys.exit(0)

try:
	writing(key)
except:		
	print "Intenta de nuevo"
	sys.exit(0)
else:	
	print "Numeros Generados"

if not os.path.exists('keys'):
    os.makedirs('keys')



