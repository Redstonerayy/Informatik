#include <iostream>
#include "vector"
#include "cmath"
#include "chrono"

void find_primes_v1(std::vector<uint32_t> primes, uint32_t MAX_PRIME)
{
	bool is_prime = true;
	uint32_t check_stopper;
	for(uint32_t prime_candidate = 3; prime_candidate < MAX_PRIME; prime_candidate++)
	{
		check_stopper = prime_candidate;
		for(uint32_t j = 2; j<=check_stopper; j++)
		{
			if(prime_candidate%j == 0)
			{
				is_prime = false;break;
			}
		}
		if(is_prime)
		{
			primes.push_back(prime_candidate);
		}
		is_prime = true;
	}
}

void find_primes_v2(std::vector<uint32_t> primes, uint32_t MAX_PRIME)
{
	bool is_prime = true;
	uint32_t check_stopper;
	for(uint32_t prime_candidate = 3; prime_candidate < MAX_PRIME; prime_candidate += 2)
	{
		check_stopper = prime_candidate;
		for(uint32_t j = 2; j<=check_stopper; j++)
		{
			if(prime_candidate%j == 0)
			{
				is_prime = false;
				break;
			}
		}
		if(is_prime)
		{
			primes.push_back(prime_candidate);
		}
		is_prime = true;
	}
}

void find_primes_v3(std::vector<uint32_t> primes, uint32_t MAX_PRIME)
{
	bool is_prime = true;
	uint32_t check_stopper;
	for(uint32_t prime_candidate = 3; prime_candidate < MAX_PRIME; prime_candidate += 2)
	{
		check_stopper = prime_candidate;
		for(uint32_t j = 3; j<=check_stopper; j += 2)
		{
			if(prime_candidate%j == 0)
			{
				is_prime = false;
				break;
			}
		}
		if(is_prime)
		{
			primes.push_back(prime_candidate);
		}
		is_prime = true;
	}
}

void find_primes_v4(std::vector<uint32_t> primes, uint32_t MAX_PRIME)
{
	bool is_prime = true;
	uint32_t check_stopper;
	for(uint32_t prime_candidate = 3; prime_candidate < MAX_PRIME; prime_candidate += 2)
	{
		check_stopper = std::sqrt(prime_candidate);
		for(uint32_t j = 3; j<=check_stopper; j += 2)
		{
			if(prime_candidate%j == 0)
			{
				is_prime = false;break;
			}
		}
		if(is_prime)
		{
			primes.push_back(prime_candidate);
		}
		is_prime = true;
	}
}
void find_primes_v5(std::vector<uint32_t> primes, uint32_t MAX_PRIME)
{
	bool is_prime = true;
	uint64_t check_stopper;
	primes.push_back(3);
	for(uint32_t prime_candidate = 5; prime_candidate < MAX_PRIME; prime_candidate += 2)
	{
		check_stopper = std::sqrt(prime_candidate);
		for(uint32_t j = 1; primes[j]<=check_stopper; j++)
		{
			if(prime_candidate%primes[j] == 0)
			{
				is_prime = false;
				break;
			}
		}
		if(is_prime)
		{
			primes.push_back(prime_candidate);
		}
		is_prime = true;
	}
}

int main() {
	std::vector<uint32_t> primes;
	std::chrono::duration<double> run_time(0.0);
	uint32_t max_prime = 256;
	int counter = 8;
	while (true) {

		for(int i = 0; i < 10; i++) {
			primes.push_back(2);
			std::chrono::time_point start = std::chrono::high_resolution_clock::now();

			find_primes_v5(primes, max_prime);

			std::chrono::time_point end = std::chrono::high_resolution_clock::now();
			run_time += end - start;
			primes.clear();
		}
		std::cout << std::endl << "Runtime for: " << counter << " Bit as max prime: ";
		std::cout << run_time.count() / 10 << std::endl;
		if(run_time.count() > 100)
		{
			break;
		}
		counter++;
		max_prime *= 2;
		run_time *= 0;
	}
}