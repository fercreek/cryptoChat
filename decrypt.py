import binascii

def decrypt(c_msg,key):
	j = 0
	plain_message = ""
	for c in c_msg:
		p = int((key[j%len(key)]))
		plain_message += str(int(c) ^ p)
		j += 1	
	return plain_message

def readCypher():
	f=open("ciphertext.txt","r")
	cipher = f.readline()
	cipher = cipher.strip()
	f.close()
	return cipher

def readKey():
	f=open("keys/keyB.txt","r")
	key = f.readline()
	key = key.strip()
	f.close()
	return key

def putting(cipher):
	ff=open("plain.txt", "w")
	ff.write(cipher)
	ff.close()

binar = decrypt(readCypher(), readKey())

bina=int(binar,2)
cipher = binascii.unhexlify('%x' % int(bina))
putting(str(cipher + '\n'))
print "Decryption success"