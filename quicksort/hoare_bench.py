def swap(array_, i1, i2):
	temp = array_[i1]
	array_[i1] = array_[i2]
	array_[i2] = temp
	return array_

def hoare_partition(array_, start, end, stats_):
	stats_["accesses"] += 1
	pivot = array_[(start + end) // 2]

	i = start - 1
	j = end + 1

	while True:
		stats_["accesses"] += 1
		stats_["checks"] += 1
		i += 1
		while array_[i] < pivot:
			i += 1

		stats_["accesses"] += 1
		stats_["checks"] += 1
		j -= 1
		while array_[j] > pivot:
			j -= 1

		stats_["checks"] += 1
		if i >= j:
			return j
		
		stats_["accesses"] += 4
		swap(array_, i, j)

def quicksort(array_, start, end, stats_):
	stats_["calls"] += 1
	stats_["checks"] += 1
	if start >= 0 and end >= 0 and start < end:
		crossing = hoare_partition(array_, start, end, stats_)

		quicksort(array_, start, crossing, stats_)
		quicksort(array_, crossing + 1, end, stats_)

# stats object
# stats = {"calls": 0, "comparisons": 0, "accesses": 0,}
