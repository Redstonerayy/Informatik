import sys

sys.setrecursionlimit(1000000)
sys.set_int_max_str_digits(5000000)

# summer von 0 - n zahlen
def f(n):
	if n == 0:
		return 0;
	else:
		return n + f(n - 1)

# factorial linear loop
def fac(n):
	fk = 1
	for i in range(1, n + 1):
		fk *= i

	return fk

# factorial recursion
def recfac(n):
	if n == 0:
		return 1
	else:
		return n * recfac(n - 1)

# reverse string
def umdrehen(word):
	if word:
		return word[-1] + umdrehen(word[:-1])
	return ""

# trianglecount
def dreieck(n):
	if n == 1:
		return 1
	return 4 + dreieck(n - 1)

# 

# print(f(100))
# print(f(5000))
# print(fac(3))
# print(recfac(9000))
# print(fac(0))
# print(recfac(0))
print(umdrehen("HALLO"))
print(dreieck(3))