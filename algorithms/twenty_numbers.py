twenty_numbers = [4, 5, 5, 2, 8, 10, 3, 2, 7, 6, 9, 9, 4, 8, 10, 9, 10, 9, 10, 6]

def dreiA():
	for i in twenty_numbers:
		if i == 8 or i == -4:
			return True
	return False

def dreiB():
	count = 0
	for i in twenty_numbers:
		if i == 10:
			count += 1
	return count

def dreiC():
	count = 0
	for i in twenty_numbers:
		if i % 2 == 0:
			count += 1
	return count
