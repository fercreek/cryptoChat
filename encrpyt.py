#msg = raw_input("Type your message to encrypt: ")
#2dxNx
f=open("keys/key.txt","r")
txt = f.readline()
f.close()
print txt
msg = "holas"
cipher = ""
for m in msg:
	for t in range(5):
		cipher += txt[t]
print cipher
