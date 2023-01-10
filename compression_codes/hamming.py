import random # get random indexes to apply noise to
import numpy as np # get random stream of "bytes"

#7, 4 hamming codes
msg = [0, 1, 1, 0] # 1,2,3,4

# function to determine the safety bits
def encode(msg):
	b1 = msg[0] + msg[1] + msg[3] # 1,2,4
	b2 = msg[0] + msg[2] + msg[3] # 1,3,4 
	b3 = msg[1] + msg[2] + msg[3] # 2,3,4
	# for each byte combination check if the number of 1's is even
	# and determine the parity bit
	b1 = 0 if b1 % 2 == 0 else 1 # bit 1
	b2 = 0 if b2 % 2 == 0 else 1 # bit 2
	b3 = 0 if b3 % 2 == 0 else 1 # bit 3
	return [*msg, b1, b2, b3] # return the 7 bits

# function to invert 0 - 7 bits
def noise(msg, amount):
	if amount > 7: # can't change more than 7 bits
		amount = 7 # set to max value if larger
	
	# sample random integers from a range, each index only comes once
	position = random.sample(range(0, 6), amount)
	# invert the bits at each sampled position
	for pos in position:
		# invert bits
		if msg[pos] == 1:
			msg[pos] = 0
		else:
			msg[pos] = 1

	return msg[:] # return the message containing the errors

# decode message, assume 0 or 1 errors
def decode(msg):
	# check if number of bits is even
	# true if even
	c1 = (msg[0] + msg[1] + msg[3] + msg[4]) % 2 == 0 # add bits and check
	c2 = (msg[0] + msg[2] + msg[3] + msg[5]) % 2 == 0 # add bits and check
	c3 = (msg[1] + msg[2] + msg[3] + msg[6]) % 2 == 0 # add bits and check
	print(c1, c2, c3)
	bits = set([0, 1, 2, 3, 4, 5, 6]) # set of indices where a bit could be wrong
	# for every parity group
	# if even(true) then (assume) no error in this group
	# remove the indices from the set of bits
	# if odd(false) then (assume) one error in this group
	# make intersect of bits and this group
	# through intersection and removing only 0 or 1 bit will remain
	if not c1: # parity group 1
		bits = bits & set([0, 1, 3, 4]) # intersect
	else:
		bits = bits - set([0, 1, 3, 4]) # remove

	if not c2: # parity group 2
		bits = bits & set([0, 2, 3, 5]) # intersect
	else:
		bits = bits - set([0, 2, 3, 5]) # remove
		
	if not c3: # parity group 3
		bits = bits & set([1, 2, 3, 6]) # intersect
	else:
		bits = bits - set([1, 2, 3, 6]) # remove

	# if a bit is in the list, and error was found
	# invert bit at this position to correct the error
	if len(list(bits)) > 0:
		# invert bit
		if msg[list(bits)[0]] == 1:
			msg[list(bits)[0]] = 0
		else:
			msg[list(bits)[0]] = 1

	return msg[:4] # return message part of code through slicing

# driver code
encoded = encode(msg)
print(encoded)
print(encoded[4:6] + [encoded[0]] + [encoded[-1]] + encoded[1:4])
noise = noise(encoded, 1)
print(noise)
decoded = decode(noise)
print(decoded)


# filestream
datastream = []
with open("input.txt") as file:
	data = file.read() # read file content as string
	for i in data: # for each character
		letter = list(bin(ord(i))[2:]) # convert into binary list
		while len(letter) < 8: # fill until 8 bits long
			letter.insert(0, "0")
		letter = [int(i) for i in letter] # conver to integers
	datastream.append(letter) # add to datastream as list of 8 elements		

# encodedstream = []
# for i in datastream:


# decode datastream
# datastream = np.random.randint(0, 2, 4 * 20)
# encodedstream = []
# for i in range(0, len(datastream), 4):
# 	encodedstream.append(encode(datastream[i: i + 4])) 

# for i in range(0, len(datastream), 4):
# 	print(datastream[i: i + 4], "  :  ", encodedstream[i//4])
