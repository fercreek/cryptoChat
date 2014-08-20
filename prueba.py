msg = '1010101010101'
key = '1110'
i = 0
print msg + " original"
crypt_message = ''
for letter in msg:
	k = int((key[i%len(key)]))
	
	crypt_message += str(int(letter) ^ k)
 	i += 1
print crypt_message + " encriptado"
j = 0
plain_message = ""
for c in crypt_message:
	p = int((key[j%len(key)]))
	plain_message += str(int(c) ^ p)
	j += 1
print plain_message + " decifrado"	

# for letter in plain_message:
# 	m = ord(letter)
# 	k = ord(key[i % len(key)])
# 	crypt_message += chr(m ^ k)
# 	i += 1