def swap(array_, i1, i2):
	temp = array_[i1]
	array_[i1] = array_[i2]
	array_[i2] = temp
	return array_

def hoare_partition(array_, start, end):
	pivot = array_[(start + end) // 2]

	i = start - 1
	j = end + 1

	while True:
		i += 1
		while array_[i] < pivot:
			i += 1

		j -= 1
		while array_[j] > pivot:
			j -= 1

		if i >= j:
			return j
		
		swap(array_, i, j)

def quicksort(array_, start, end):
	if start >= 0 and end >= 0 and start < end:
		crossing = hoare_partition(array_, start, end)

		quicksort(array_, start, crossing)
		quicksort(array_, crossing + 1, end)

liste = [3, 4, 1, 6, 7, 2, 1, 1, 0, 6]
quicksort(liste, 0, len(liste) - 1)
print(liste)
