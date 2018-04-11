from script import shifting,sub 
from collections import deque

alphabet = list('abcdefghijklmnopqrstuvwxyz{}_')
maping = {}
clear = ''

# Create MAP

for i in range(0,len(alphabet)):
	clear = shifting(alphabet[i])
	maping [alphabet[i]] = clear

# Get The cipher and rotate it

file = open('ciphertext.txt','r').read()
cipher = deque(list(file))
cipher.rotate(3)


# MAPING

plaintext=''

for c in cipher:
	plaintext += maping[c]

print plaintext
