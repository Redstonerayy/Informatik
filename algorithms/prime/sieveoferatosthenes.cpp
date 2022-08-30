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
            // std::cout << i << ":" << i - offset << "pos" << "\n";
            if(i >= limit){
                break;
            }
            if(!marks[i - offset]){ //is prime
                // std::cout << i << ":";
                // std::cout << i - offset << ":" << offset + chunksize << "\n";
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
    
    // calcprimeu64(limit64);
    // calcprimeu32(limit32);
    // calcimprovedsieve64(limit64);
    offsetsieve(std::pow(2,30), std::pow(2,30));
    // offsetsieve(20);
}
