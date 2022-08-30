# generate primes
def genprimes(limit):
	primes = []
	marks = [True for i in range(limit)]
	i = 2
	while i < limit:
		if marks[i]:
			primes.append(i)
			j = i + i
			while(j < limit):
				marks[j] = False
				j += i
		
		i += 1

	return primes

print(len(genprimes(2 ** 27)))
