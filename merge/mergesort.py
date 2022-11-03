import random

# set seed so output is comparable
random.seed(10)

def swap(array_, i1, i2):
	temp = array_[i1]
	array_[i1] = array_[i2]
	array_[i2] = temp

# generate random list, which is sorted
def gen(length : int):
	liste = [random.randint(0, 100) for i in range(length)]
	return liste

def mergesort(_array, start, end):
	if end - start == 0:
		return
	elif end - start == 1:
		if _array[start] > _array[end]:
			swap(_array, start, end)
	else:
		# sort parts
		middle = start + (end - start) // 2
		mergesort(_array, start, middle)
		mergesort(_array, middle + 1, end)
		# merge parts
		i = start
		j = middle + 1
		k = middle
		while i < middle and j < end:
			if _array[i] < _array[j]:
				i += 1
			else:
				swap(_array, j, k)
				j += 1
				k -= 1

liste = gen(4)
print(liste)
mergesort(liste, 0, len(liste) - 1)
print(liste)
