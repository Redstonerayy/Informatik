# https://www.geeksforgeeks.org/quick-sort/
import random

random.seed(4)

def gen(length, max):
	return [random.randint(0,max) for i in range(length)]

def swap(array_, i1, i2):
	temp = array_[i1]
	array_[i1] = array_[i2]
	array_[i2] = temp
	return array_

def quicksort(array_, start, end):
	if start >= end:
		return
	pivot = array_[end]

	i = start - 1

	for j in range(start, end):
		if array_[j] < pivot:
			i += 1
			swap(array_, i, j)

	swap(array_, i + 1, end)

	quicksort(array_, start, i)
	quicksort(array_, i + 2, end)

liste = gen(10, 10)
print(liste)
quicksort(liste, 0, len(liste) - 1)
print(liste)
