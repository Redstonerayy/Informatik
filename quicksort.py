# https://www.geeksforgeeks.org/quick-sort/
import random

random.seed(4)

def gen(length, max):
	return [random.randint(0,max) for i in range(length)]

def quicksort(array_, start, end):
	pivot = array_[end]

	i = start - 1

	for j in range(end):
		if array_[j] < array_[end]:
			i += 1
			temp = array_[j]
			array_[j] = array_[i]
			array_[i] = temp

	temp = array_[end]
	array_[end] = array_[i + 1]
	array_[i + 1] = temp
	print(array_)
	print(start, i)
	print(i + 2, end)
	return i

liste = gen(10, 10)
print(liste)
quicksort(liste, 0, len(liste) - 1)
