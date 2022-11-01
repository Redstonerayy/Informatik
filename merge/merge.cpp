#include <iostream>
#include <vector>
#include <random>
#include <algorithm>

std::vector<int> gen(int length){
	std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_int_distribution<std::mt19937::result_type> dist(1,10);
	
	std::vector<int> array;
	for(int i = 0; i < length; ++i){
		array.emplace_back(dist(rng));
	}
	return array;
}

void printvector(std::vector<int> &v){
	for(int &el : v){
		std::cout << el << " ";
	}
	std::cout << std::endl;
}

std::vector<int> merge(std::vector<int> &v1, std::vector<int> &v2){
	int i = 0;
	int j = 0;
	std::vector<int> result;
	while(i < v1.size() && j < v2.size()){
		if(v1[i] < v2[j]){
			result.emplace_back(v1[i])
			++i;
		} else {
			result.emplace_back(v2[j])
			++j;
		}
	}

	if(i < v1.size()){
		result.insert(result.end(), v1.at(i), v1.end());
	} else {
		result.insert(result.end(), v2.at(i), v2.end());
	}

	return result;
}

int main(){
	std::vector<int> l1 = gen(10);
	std::vector<int> l2 = gen(10);
	printvector(l1);
	printvector(l2);
	
	std::vector<int> lg = merge(l1, l2);

	return 0;
}