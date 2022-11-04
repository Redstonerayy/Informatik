import sys

sys.setrecursionlimit(1000000)
sys.set_int_max_str_digits(5000000)

def f(n):
	if n == 0:
		return 0;
	else:
		return n + f(n - 1)

def fac(n):
	fk = 1
	for i in range(1, n + 1):
		fk *= i

	return fk

def recfac(n):
	if n == 0:
		return 1
	else:
		return n * recfac(n - 1)

print(f(100))
print(f(5000))
print(fac(3))
print(recfac(19000))
print(fac(0))
print(recfac(0))