import binascii

def readLine():
	f=open("keys/key.txt","r")
	key = f.readline()
	key = key.strip()
	f.close()
	# global bina
	# bina =  bin(int(binascii.hexlify(key), 16))
	# bina = bina[2:]
	return key

def crypt(key):
	i = 0
	crypt_message = ''
	for letter in msg:
		k = int((key[i%len(key)]))
		crypt_message += str(int(letter) ^ k)
	 	i += 1
	return crypt_message

def decrypt(crypt_message,key):
	j = 0
	plain_message = ""
	for c in crypt_message:
		p = int((key[j%len(key)]))
		plain_message += str(int(c) ^ p)
		j += 1	
	return plain_message


msg = 'hola'
msg = bin(int(binascii.hexlify(msg), 16))
msg = msg[2:]
a = readLine()	
c = crypt(a)
p = decrypt(c,a)

change = int(c)
n = int('110100001100101011011000110110001101111', 2)
print type(change)
print binascii.unhexlify('%x' % int(change)