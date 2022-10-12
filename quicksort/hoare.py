# swap 2 elements of array
def swap(array_, i1, i2):
	temp = array_[i1]
	array_[i1] = array_[i2]
	array_[i2] = temp
	return array_

# partition range of the array
def hoare_partition(array_, start, end):
    # use middle element as pivot, faster on sorted arrays
	pivot = array_[(start + end) // 2]

    # 2 counters
	i = start - 1
	j = end + 1

    # repeat until the 2 pointers meet
	while True:
        # move forward by one, do this before loop to prevent beeing stuck at
        # an inversed element pair
		i += 1
        # if the element is smaller than the pivot, it can stay there
        # check the next element
		while array_[i] < pivot:
			i += 1

        # go back by one, do this before loop to prevent beeing stuck at
        # an inversed element pair
		j -= 1
        # if the element is bigger than the pivot, it can stay there
        # check the next element
		while array_[j] > pivot:
			j -= 1

        # if both loops finish, either the pointers crossed
        # which is checked here, or the left one is on a bigger 
        # and the right one on a smaller value
        # so these elements should be swapped

		if i >= j:
			return j
		
		swap(array_, i, j)

# recursive function
def quicksort(array_, start, end):
	if start >= 0 and end >= 0 and start < end:
		crossing = hoare_partition(array_, start, end)

        # recursively call the function
        # left side, from start to the positon the rightmost smaller element
		# is or was swapped to
		quicksort(array_, start, crossing)
		# right side, from the element right to the rightmost smaller element,
        # to the end of the previous range
		quicksort(array_, crossing + 1, end)

# sort list
liste = [3, 4, 1, 6, 7, 2, 1, 1, 0, 6]
quicksort(liste, 0, len(liste) - 1)
print(liste)
