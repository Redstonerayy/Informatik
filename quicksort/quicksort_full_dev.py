# https://www.geeksforgeeks.org/quick-sort/
import random

random.seed(4)

def median(threelements_):
	threelements_.sort()
	return threelements_[1]

def gen(length, max):
	return [random.randint(0,max) for i in range(length)]

def swap(array_, i1, i2):
	temp = array_[i1]
	array_[i1] = array_[i2]
	array_[i2] = temp
	return array_

def hoare_partition(array_, start, end):
	pivot = array_[(start + end) // 2]
	print("Pivot", pivot)

	i = start - 1
	j = end + 1

	while True:
		i += 1
		while array_[i] < pivot:
			i += 1

		j -= 1
		while array_[j] > pivot:
			j -= 1

		print(array_)
		print("Pointers", i, j)
		if i >= j:
			return j
		
		swap(array_, i, j)

def hoare(array_, start, end):
	if start >= 0 and end >= 0 and start < end:
		crossing = hoare_partition(array_, start, end)

		hoare(array_, start, crossing)
		hoare(array_, crossing + 1, end)



def quicksort(array_, start, end):
	if start >= end or start < 0:
		return
	pivot = array_[end]

	i = start - 1

	for j in range(start, end):
		if array_[j] < pivot:
			i += 1
			swap(array_, i, j)

	swap(array_, i + 1, end)

	print(array_)

	quicksort(array_, start, i)
	quicksort(array_, i + 2, end)

liste = gen(10, 10)
print(liste)
print("-----")
# quicksort(liste, 0, len(liste) - 1)
hoare(liste, 0, len(liste) - 1)
print("-----")
print(liste)

"""
* Lomuto(simple, slow) vs Hoare(complex, approx 3x faster) partition
* Use insertion sort if length of list is small
* random(slow generation, good against malicious input??), 
  middle or median element(best), first/last is slow for sorted input, worst case

https://en.wikipedia.org/wiki/Quicksort
https://en.wikipedia.org/wiki/Insertion_sort
https://en.wikipedia.org/wiki/Median
https://stackoverflow.com/questions/7559608/median-of-three-values-strategy

"""
