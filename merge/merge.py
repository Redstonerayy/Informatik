import random

# set seed so output is comparable
random.seed(10)

# generate random list, which is sorted
def gen(length : int):
	liste = [random.randint(0, 100) for i in range(length)]
	liste.sort()
	return liste

# sort an array consisting of to sorted parts
# return a new sorted combination of both
def merge(_array, middle):
	# initialize counters and output array
	i = 0
	j = middle
	result = []
	# compare and add elements
	while i < middle and j < len(_array):
		if _array[i] < _array[j]:
			result.append(_array[i])
			i += 1
		else:
			result.append(_array[j])
			j += 1

	# add rest of the unfinished array
	if i < middle:
		result += _array[i:middle]
	else:
		result += _array[j:]

	return result

# testing
l1 = gen(10)
l2 = gen(10)
lg = l1 + l2
print(l1)
print(l2)
print(merge(lg, 10))

