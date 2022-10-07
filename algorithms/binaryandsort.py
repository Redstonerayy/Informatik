import random

# generate list with random number from 1 to 1000
def generate_array(laenge):
	liste = []
	for i in range(laenge):
		liste.append(random.randint(1, 100))
	return liste

def easy_gen():
	liste = [i for i in range(100)]
	random.shuffle(liste)
	return liste

def binaeres_suchen(number, numberarray):
	index = -1
	found = False
	links = 0
	checks = 0
	rechts = len(numberarray)-1
	while not found and links <= rechts:
		checks += 1
		mitte = (links + rechts) // 2
		if number == numberarray[mitte]:
			found = True
			index = mitte
		elif number < numberarray[mitte]:
			rechts = mitte-1
		else:
			links = mitte+1
	
	return index, checks


def sort_list(liste):
	n = len(liste) - 1
	while not n < 1:
		swap = False
		for i in range(n):
			if liste[i] > liste[i + 1]:
				swap = True
				# needed?
				temp = liste[i]
				liste[i] = liste[i + 1]
				liste[i + 1] = temp
		
		if not swap:
			break
			
		n -= 1
	
	return liste

liste = easy_gen()
print(liste)
liste = sort_list(liste)
print(liste)


print(binaeres_suchen(random.randint(0, 99), liste))
