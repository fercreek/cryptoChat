#!/usr/bin/python
import string
import os
from random import choice
def keys(amount, key_len):
	totalKeys = ""
	r = '10'
	for a in range(amount):
		kl = ""
		for k in range(key_len):
			kl += choice(r)
		totalKeys += kl + '\n'
	return totalKeys

amount = input("Type the amount of keys: ")
key_len = input("Type the length of the key: ")

a = keys(amount, key_len)

if not os.path.exists('keys'):
    os.makedirs('keys')

f=open("keys/keyA.txt","w")
f.write(a)
f.close()
f=open("keys/keyB.txt","w")
f.write(a)
f.close()

