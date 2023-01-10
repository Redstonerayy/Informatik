werte = [84, 62, 46, 38, 24, 18, 16, 10, 8, 6, 4]
sume = 0

for i in range(1, len(werte)):
	sume += werte[i] * 10 + ((werte[i - 1] - werte[i]) * 10) / 2

print(sume)