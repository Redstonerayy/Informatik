#include <iostream>
#include <vector>
#include <cstdint> //use std::uint64_t, its guaranted to be in std:: namespace
#include <string>
#include <cmath>

void offsetsieve(std::uint64_t limit, std::uint64_t chunksize){
    std::vector<uint64_t> primes;
    std::vector<uint64_t> primecomposites;
    std::uint64_t offset = 2;
    if(chunksize > limit){
        chunksize = limit;
    }

    while(offset < limit){
        std::vector<bool> marks(chunksize);

        //mark known primes
        for(std::uint64_t i = 0; i < primecomposites.size(); ++i){
            while(primecomposites[i] < offset + chunksize){
                marks[primecomposites[i] - offset] = true;
                primecomposites[i] += primes[i];
            }
        }
        
        for(std::uint64_t i = offset; i < offset + chunksize; ++i){
            if(i >= limit){
                break;
            }
            if(!marks[i - offset]){ //is prime
                primes.push_back(i);
                primecomposites.push_back(i + i);
                for(std::uint64_t j = i + i; j < offset + chunksize; j += i){
                    marks[j - offset] = true;
                    primecomposites[primecomposites.size() - 1] += i;
                }
            }
        }
        offset += chunksize;
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
    
    offsetsieve(limit64, std::pow(2,30));
}
