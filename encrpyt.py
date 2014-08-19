import binascii
msg = raw_input("Type your message to encrypt: ")
#10001

f=open("keys/key.txt","r")
txt = f.readline()
txt = txt.strip()
f.close()
bina =  bin(int(binascii.hexlify(msg), 16))
bina = bina[2:]
# print bina 

cipher = ""

val= int(bina,2)^int(txt,2)
cipher = bin(val)
# print cipher[2:]

n = int(bina, 2)
o = int(cipher,2)
# print binascii.unhexlify('%x' % n)
# print binascii.unhexlify('%x' % o) 
new_cipher = ""
#for r in range(1,len(msg)+1):
a = 0
b = 0
print str(len(msg)) + " " + str(len(txt))
while len(msg) != len(txt):
	(a,b) = (max(a,b),min(a,b))
	print type(a)
	print type(b)

	print type(val)

	new_cipher += txt*val
	print new_cipher
print "wii"	 