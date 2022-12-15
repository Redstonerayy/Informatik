import random
import numpy as np

#7, 4 hamming codes
msg = [1, 0, 0, 1] # 1,2,3,4

def encode(msg):
	b1 = msg[0] + msg[1] + msg[3] # 1,2,4
	b2 = msg[0] + msg[2] + msg[3] # 1,3,4 
	b3 = msg[1] + msg[2] + msg[3] # 2,3,4
	b1 = 0 if b1 % 2 == 0 else 1
	b2 = 0 if b2 % 2 == 0 else 1
	b3 = 0 if b3 % 2 == 0 else 1
	return [*msg, b1, b2, b3]

def noise(msg, amount):
	if amount > 7:
		amount = 7
	
	position = random.sample(range(0, 6), amount)
	for pos in position:
		if msg[pos] == 1:
			msg[pos] = 0
		else:
			msg[pos] = 1

	return msg

def decode(msg):
	# check if number of bits is even
	# true if even
	c1 = (msg[0] + msg[1] + msg[3] + msg[4]) % 2 == 0
	c2 = (msg[0] + msg[2] + msg[3] + msg[5]) % 2 == 0
	c3 = (msg[1] + msg[2] + msg[3] + msg[6]) % 2 == 0
	bits = set([0, 1, 2, 3, 4, 5, 6])
	print(c1, c2, c3)
	if not c1:
		bits = bits & set([0, 1, 3, 4]) 
	else:
		bits = bits - set([0, 1, 3, 4])

	if not c2:
		bits = bits & set([0, 2, 3, 5])
	else:
		bits = bits - set([0, 2, 3, 5])
		
	if not c3:
		bits = bits & set([1, 2, 3, 6])
	else:
		bits = bits - set([1, 2, 3, 6])

	print(bits)
	if len(list(bits)) > 0:
		if msg[list(bits)[0]] == 1:
			msg[list(bits)[0]] = 0
		else:
			msg[list(bits)[0]] = 1

	return msg[:4]

encoded = encode(msg)
print(encoded)
noise = noise(encoded, 1)
print(noise)
decoded = decode(noise)
print(decoded)

# decode datastream
datastream = np.random.randint(0, 2, 4 * 20)
print(datastream)

encodedstream = []
for i in range(0, len(datastream), 4):
	encodedstream += encode(datastream[i: i + 4])

print(encodedstream)