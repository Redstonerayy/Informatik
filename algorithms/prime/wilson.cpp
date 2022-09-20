#include <bits/stdc++.h>

// Function to calculate the factorial
std::uint64_t fact(const std::uint64_t& p)
{
    if (p <= 1)
        return 1;
    return p * fact(p - 1);
}
 
// Function to check if the
// number is prime or not
bool isPrime(const std::uint64_t& p)
{
    if (p == 4)
        return false;
    return bool(fact(p >> 1) % p);
}
 
// Driver code
int main(int argc, char** argv)
{
	std::cout << isPrime(std::stoull(argv[1])) << std::endl;
}
