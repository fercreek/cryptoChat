import binascii

def readKey():
	f=open("keys/keyA.txt","r")
	key = f.readline()
	key = key.strip()
	f.close()
	return key

def crypt(key):
	i = 0
	c_msg = ''
	for letter in msg:
		k = int((key[i%len(key)]))
		c_msg += str(int(letter) ^ k)
	 	i += 1
	return c_msg

def writeText(cipher):
	ff=open("ciphertext.txt", "wb")
	ff.write(cipher)
	ff.close()

def eraseKey():
	f=open("keys/keyA.txt", "r")
	firstL= f.readline()
	lines=f.readlines()
	f.close()
	f=open("keys/keyA.txt", "w")
	for line in lines:
		if line!=firstL:
			f.write(line)
	f.close()

msg = raw_input("Type a text: ")
msg = bin(int(binascii.hexlify(msg), 16))
msg = msg[2:]
a = readKey()	

writeText(crypt(a))
eraseKey()
print "Encryption success"