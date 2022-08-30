#include <iostream>
#include <vector>
#include <cstdint> //use std::uint64_t, its guaranted to be in std:: namespace
#include <string>
#include <math.h>
#include <unordered_map>

void badcalcimprovedsieve64(std::uint64_t limit){
    std::vector<std::uint64_t> primes;
    std::vector<std::uint64_t> composites;
    for(std::uint64_t i = 2; i < limit; ++i){
        bool prime = true;
        //check if it a composite
        for(std::uint64_t j = 0; j < composites.size(); ++j){
            if(i == composites[j]){
                composites[j] += primes[j];
                prime = false;
            }
        }
        //add it to primes, generate its composite
        if(prime){
            primes.push_back(i);
            composites.push_back(i + i);
        }
    }

    //print primes
    // for(std::uint64_t i = 0; i < primes.size(); ++i){
    //     std::cout << primes[i] << "\n";
    // }
    std::cout << "Length: " << primes.size() << "\n";
}

void calcimprovedsieve64(std::uint64_t limit){
    std::vector<std::uint64_t> primes;
    // std::vector<std::uint64_t> composites;
    // std::unordered_map<std::uint64_t, std::uint64_t> primes;
    // std::unordered_map<std::uint64_t, bool> composites;
    std::unordered_map<std::uint64_t, std::vector<std::uint64_t>> primecomposites; //composite, prime
    for(std::uint64_t i = 2; i < limit; ++i){
        //check if it a composite
        if(primecomposites[i].size() > 0){
            //std::cout << i << "\n";
            for(int j = 0; j < primecomposites[i].size(); ++j){
                if(primecomposites.contains(i + primecomposites[i][j])){
                    primecomposites[i + primecomposites[i][j]].push_back(primecomposites[i][j]);
                } else {
                    primecomposites[i + primecomposites[i][j]] = std::vector<std::uint64_t> { primecomposites[i][j] };
                }
            }

            primecomposites.erase(i);
        } else {
            primes.push_back(i);
            primecomposites[i + i] = std::vector<std::uint64_t> { i };
        }
    }

    //print primes
    // for(std::uint64_t i = 0; i < primes.size(); ++i){
    //     std::cout << primes[i] << "\n";
    // }
    
    std::cout << "Length: " << primes.size() << "\n";
}

//grab input args
int main(int argc, char** argv){
    //define limit
    std::uint64_t limit64;
    std::uint32_t limit32;
    //potentially make custom limit
    if(argc > 1){
        limit64 = std::stoi(argv[1]);
        limit64 = std::pow(2, limit64);
        limit32 = std::stoi(argv[1]);
        limit32 = std::pow(2, limit32);
    } else {
        limit64 = std::pow(2, 16);
        limit32 = std::pow(2, 16);
    }
    
    badcalcimprovedsieve64(limit64);
	calcimprovedsieve64(limit64);
}
