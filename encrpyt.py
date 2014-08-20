import binascii

def readLine():
	f=open("keys/key.txt","r")
	key = f.readline()
	key = key.strip()
	f.close()
	global bina
	bina =  bin(int(binascii.hexlify(key), 16))
	bina = bina[2:]
	return key

def crypt(key):
	i = 0
	crypt_message = ''
	for letter in bina:
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

a = readLine()	
c = crypt(a)
p = decrypt(c,a)

print bina
print c + "encript"
print p + 'decrypt'
print a*8