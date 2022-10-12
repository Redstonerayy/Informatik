def swap(array_, i1, i2):
	temp = array_[i1]
	array_[i1] = array_[i2]
	array_[i2] = temp
	return array_

def lomuto_partition(array_, start, end, stats_):
	stats_["accesses"] += 1
	pivot = array_[end]

	i = start - 1

	for j in range(start, end):
		stats_["accesses"] += 1
		stats_["checks"] += 1
		if array_[j] < pivot:
			i += 1
			stats_["accesses"] += 4
			swap(array_, i, j)

	stats_["accesses"] += 4
	swap(array_, i + 1, end)

	return i

def quicksort(array_, start, end, stats_):
	stats_["calls"] += 1
	stats_["checks"] += 1
	if not (start >= end or start < 0):
		edge = lomuto_partition(array_, start, end, stats_)

		quicksort(array_, start, edge, stats_)
		quicksort(array_, edge + 2, end, stats_)

# stats object
# stats = {"calls": 0, "checks": 0, "accesses": 0,}
