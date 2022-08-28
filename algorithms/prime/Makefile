.PHONY: cppprime
cppprime:
	g++ -O3 -mavx2 -std=c++20 -march=native primeanton.cpp -o primeanton
	g++ -O3 -mavx2 -std=c++20 -march=native sieveoferatosthenes.cpp -o eratosthenes
	./eratosthenes

clean:
	rm primeanton
	rm eratosthenes