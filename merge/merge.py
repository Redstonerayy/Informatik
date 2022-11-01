import random

random.seed(10)

def gen(length : int):
	liste = [random.randint(0, 100) for i in range(length)]
	liste.sort()
	return liste

def merge(_array, middle):
	i = 0
	j = middle
	result = []
	while i < middle and j < len(_array):
		if _array[i] < _array[j]:
			result.append(_array[i])
			i += 1
		else:
			result.append(_array[j])
			j += 1

	if i < middle:
		result += _array[i:middle]
	else:
		result += _array[j:]

	return result

l1 = gen(10)
l2 = gen(10)
lg = l1 + l2
print(l1)
print(l2)
print(merge(lg, 10))

