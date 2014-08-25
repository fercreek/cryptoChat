def decrypt(crypt_message,key):
	j = 0
	plain_message = ""
	for c in crypt_message:
		p = int((key[j%len(key)]))
		plain_message += str(int(c) ^ p)
		j += 1	
	return plain_message