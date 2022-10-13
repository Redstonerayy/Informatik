def bubblesort(liste, stats_):
	stats_["calls"] += 1
	n = len(liste) - 1
	while not n < 1:
		swap = False
		for i in range(n):
			stats_["accesses"] += 2
			stats_["checks"] += 1
			if liste[i] > liste[i + 1]:
				swap = True
				# needed?
				stats_["accesses"] += 4
				temp = liste[i]
				liste[i] = liste[i + 1]
				liste[i + 1] = temp
		
		stats_["checks"] += 1
		if not swap:
			break

		n -= 1