def swap(array_, i1, i2):
	temp = array_[i1]
	array_[i1] = array_[i2]
	array_[i2] = temp
	return array_

def lomuto_partition(array_, start, end):
	pivot = array_[end]

	i = start - 1

	for j in range(start, end):
		if array_[j] < pivot:
			i += 1
			swap(array_, i, j)

	swap(array_, i + 1, end)

	return i

def quicksort(array_, start, end):
	if not (start >= end or start < 0):
		edge = lomuto_partition(array_, start, end)

		quicksort(array_, start, edge)
		quicksort(array_, edge + 2, end)

liste = [3, 4, 1, 6, 7, 2, 1, 1, 0, 6]
quicksort(liste, 0, len(liste) - 1)
print(liste)
