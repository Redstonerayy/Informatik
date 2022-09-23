import math
# Aufgabe 1
# function to calculate average
def average(values):
	sum = 0
	for i in values:
		sum += i

	return sum/len(values)


tanken = [123, 134, 120, 122]

print("Aufgabe 1")
print(average(tanken))

# Aufgabe 2
# function to calculate matching value
def match(first, second):
	match = 0
	shortest = len(first) if len(first) <= len(second) else len(second)
	longest = len(first) if len(first) >= len(second) else len(second)
	for i in range(shortest):
		if first[i] == second[i]:
			match += 1
	return math.floor((match/longest) * 100)

persons = [
	[True, True, False, False, False, True],
	[True, True, True, False, False, True],
	[False, False, True, True, True, False],
	[True, True, False, False, False],
]

print("Aufgabe 2")
for i in persons:
	print(match(persons[0], i), f"% with person {persons.index(i)}")

# Aufgabe 3
def getmindistance(numberarray):
	shortest = abs(numberarray[0] - numberarray[1]) 
	index = 0
	for i in range(1, len(numberarray) - 1):
		diff = abs(numberarray[i] - numberarray[i + 1])
		if shortest > diff:
			shortest = diff
			index = i

	return index


numbers = [
	[4, 8, 6, 1, 2, 9, 4],
	[33, 8, 2, 6, 43, 54],
]

print("Aufgabe 3")
for i in numbers:
	print("Index: ", getmindistance(i))


# kleinste zahl der liste
def getallmindisctance(numberarray):	
	shortest = None
	indexes = None
	for i in range(len(numberarray) - 1):
		for j in range(i + 1, len(numberarray) - 1):
			diff = abs(numberarray[i] - numberarray[j])
			if shortest == None or shortest > diff:
				shortest = diff
				indexes = [i, j]

	return indexes



print("Aufagbe 3 Advanced")
for i in numbers:
	indexes = getallmindisctance(i)
	print(i[indexes[0]], i[indexes[1]])
