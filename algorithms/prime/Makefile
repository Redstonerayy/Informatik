.PHONY: build
build:
	clang++ -O3 -mavx2 -std=c++20 -march=native sieveoferatosthenes.cpp -o eratosthenes

clean:
	rm primeanton
	rm eratosthenes

run: build
	./eratosthenes