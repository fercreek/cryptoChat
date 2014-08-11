import binascii
import sys

def toBinary(word):
	b =  bin(int(binascii.hexlify(word), 16))
	global val 
	val = b.replace('0b','0')
	print val + " paso 1, binario original"
	
def toString():	
	n = int(val, 2)
	print binascii.unhexlify('%x' % n) + "       paso 2, texto"


def binToCipher(val):
	cipher =""
	#val    01101000
	key =  '0101010'
	a = int(val,2) ^ int(key,2)
	global cip
	cip = bin(int(a))
	cip = cip.replace('0b','0')
	print cip + " paso 3, binario a cipher"

def CipherToBin(cip):
	key =  '10101010'
	a = int(cip,2) ^ int(key,2)
	global plain
	plain = bin(int(a))
	plain = plain.replace('0b','0')
	print plain + " paso 4, cipher a binario"

def normal(plain):
	n = int(plain, 2)
	print binascii.unhexlify('%x' % n) + "       paso 5, texto"

toBinary(sys.argv[1])
toString()
binToCipher(val)
CipherToBin(cip)
normal(plain)