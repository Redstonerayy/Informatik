#7, 4 hamming codes
msg = [1, 0, 0, 1]


def encode(msg):
	b1 = msg[0] + msg[1] + msg[3] # 1,2,4
	b2 = msg[0] + msg[2] + msg[3] # 1,3,4 
	b3 = msg[1] + msg[2] + msg[3] # 2,3,4
	b1 = 0 if b1 % 2 == 0 else 1
	b2 = 0 if b1 % 2 == 0 else 1
	b3 = 0 if b1 % 2 == 0 else 1
	return [*msg, b1, b2, b3]

# def decode():

# def check():

# def noise():

print(encode(msg))