#include <iostream>
#include <cstdint>
#include <vector>
#include <string>

uint64_t getelementCount(const int BITS) {
    
    uint64_t elementCount = 2;
    
    for(int i = 1; i < BITS; i++)
        elementCount *= 2;
    
    return elementCount;
}

void calculate_primes(const int BITS) {
    
    const uint64_t elementscount = getelementCount(BITS);
    std::vector<bool> primecandidates(elementscount);
    std::fill(primecandidates.begin(), primecandidates.end(), true);
    
    primecandidates[0] = false;
    primecandidates[1] = false;
    
    primecandidates.shrink_to_fit();
    
    std::vector<uint64_t> primes;
    
    uint64_t offset = 0;
    uint64_t index = 0;

    while (offset < elementscount) {
        index = offset;
        while(primecandidates[index] == 0 && index < elementscount) {
            ++index;
        }
        if(index == elementscount)
            break;
        offset = index;
        primes.push_back(index);
        index = 1;
        while(index*offset < elementscount) {
            primecandidates[index*offset] = false;
            index++;
        }
    }
}

int main(int argc, char** argv) {
    if(argc > 1)
        calculate_primes(std::stoi(argv[1]));
    return 0;
}