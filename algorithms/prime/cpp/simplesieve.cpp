#include <iostream>
#include <vector>
#include <cstdint> //use std::uint64_t, its guaranted to be in std:: namespace
#include <string>
#include <math.h>
#include <unordered_map>

void calcprimeu64(std::uint64_t limit){
    //define vectors
    std::vector<std::uint64_t> primes;
    std::vector<std::uint64_t> numbers(limit + 1); //does this cause a copy? //is initialized with zeros
    
    //fill vector with numbers 2 to limit
    for(std::uint64_t i = 2; i < limit; ++i){
        numbers[i] = i; //use position because push_back ads to the end
    }
    //iterrate over each number
    //if it is zero it has been marked
    //for each prime set all composites to zero
    for(std::uint64_t i = 2; i < limit; ++i){
        std::uint64_t num = numbers[i]; //does this make it faster?
        if(num){
            primes.push_back(num);
            for(std::uint64_t j = num * num; j < limit; j += num){
                numbers[j] = 0;
            }
        }
    };
    //print primes
    // for(std::uint64_t i = 0; i < primes.size(); ++i){
    //     std::cout << primes[i] << "\n";
    // }
    std::cout << "Length: " << primes.size() << "\n";
}

void calcprimeu32(std::uint32_t limit){
    //define vectors
    std::vector<std::uint32_t> primes;
    std::vector<std::uint32_t> numbers(limit + 1); //does this cause a copy? //is initialized with zeros
    
    //fill vector with numbers 2 to limit
    for(std::uint32_t i = 2; i < limit; ++i){
        numbers[i] = i; //use position because push_back ads to the end
    }
    //iterrate over each number
    //if it is zero it has been marked
    //for each prime set all composites to zero
    for(std::uint32_t i = 2; i < limit; ++i){
        std::uint32_t num = numbers[i]; //does this make it faster?
        if(num){
            primes.push_back(num);
            for(std::uint32_t j = num * num; j < limit; j += num){
                numbers[j] = 0;
            }
        }
    };
    //print primes
    // for(std::uint32_t i = 0; i < primes.size(); ++i){
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
    
    calcprimeu64(limit64);
    calcprimeu32(limit32);
}
