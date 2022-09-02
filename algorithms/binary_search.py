"""
Binary Search
1:
a) mittleres linkes element
b) pro suche werden jeweils die haelfte der stellen ausgeschlossen
c) der index ist negativ, also -1
"""


import random
import string

def generate_array(laenge):
	liste = []
	for i in range(laenge):
		liste.append(random.choice(string.ascii_lowercase))
	return liste

def binaeres_suchen(buchstabe, reihung):
	indexErgebnis = -1
	gefunden = False
	links = 0
	check = 0
	rechts = len(reihung)-1
	while not gefunden and links <= rechts:
		check += 1
		mitte = (links + rechts) // 2
		if buchstabe == reihung[mitte]:
			gefunden = True
			indexErgebnis = mitte
		elif buchstabe < reihung[mitte]:
			rechts = mitte-1
		else:
			links = mitte+1
	
	return indexErgebnis, check

def test_search(num):
	for i in range(num):
		hightest = -1
		for j in range(100):
			index, accesses = binaeres_suchen("a", generate_array(2 ** i))
			if accesses > hightest:
				hightest = accesses
		print(i, hightest, 2 ** i)

def check_million():
	i = 20
	print(2 ** i)
	hightest = -1
	for j in range(10):
		index, accesses = binaeres_suchen("a", generate_array(2 ** i))
		if accesses > hightest:
			hightest = accesses
	print(i, hightest, 2 ** i)

test_search()
check_million()
