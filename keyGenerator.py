#!/usr/bin/python
import string
import os
from random import choice
def keys(amount, key_len):
	totalKeys = []
	r = string.ascii_letters + string.digits
	for a in range(amount):
		kl = ""
		for k in range(key_len):
			kl += choice(r)
		totalKeys.append(kl)
	return totalKeys

amount = input("Type the amount of keys: ")
key_len = input("Type the length of the key: ")

a = keys(amount, key_len)

if not os.path.exists('keys'):
    os.makedirs('keys')

print a
f=open("keys/key.txt","w")
f.write("hola")
f.close()
