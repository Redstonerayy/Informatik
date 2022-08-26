#include <iostream>
#include <math.h>
#include <vector>

//Quake III fast inverse squareroot
float Q_rsqrt( float number ) {
	long i;
	float x2, y;
	const float threehalfs = 1.5F;

	x2 = number * 0.5F;
	y  = number;
	i  = * ( long * ) &y;                       // evil floating point bit level hacking
	i  = 0x5f3759df - ( i >> 1 );               // what the fuck? 
	y  = * ( float * ) &i;
	y  = y * ( threehalfs - ( x2 * y * y ) );   // 1st iteration
	//	y  = y * ( threehalfs - ( x2 * y * y ) );   // 2nd iteration, this can be removed

	return y;
}

bool isprime(int number, bool roots){
	int lastsquareroot;
	if(roots){
		// lastsquareroot = Q_rsqrt((float)number);
		lastsquareroot = std::sqrt(number);
		if(lastsquareroot * lastsquareroot == number){
			lastsquareroot = 1;
		}
	} else {
		lastsquareroot = 1;
	}

	// std::cout << (number/lastsquareroot) << ":" << lastsquareroot << std::endl;

	if(number > 1){
		int maxtestnumber = (number/lastsquareroot);
		for(int i = 2; i < maxtestnumber; i++){
			if(number % i == 0){
				return false;
			}
		}
		return true;
	}
	return false;
}


int main(){
	std::vector<int> primes;
	for(int i = 0; i < 600000; i++){
		if(isprime(i, true)){
			primes.push_back(i);
		}
	}
	
	std::cout << primes.size() << std::endl;
	std::cout << primes[0] << std::endl;
	std::cout << primes[primes.size() - 1] << std::endl;
}