# program to check if a number is prime

import time, math

# shortening the check loop by using incomplete prime detection makes it faster
# fails to detect primes until the square of the efficient
# efficient 9 returns 4,6,8 and 9 as valid prime numbers
# calculate the last square root and use it as efficient if the square is not the same as the number

def isprime(number, roots):
    #calculate lastsquareroot
    if roots:
        lastsquareroot = math.floor(math.sqrt(number))
        if lastsquareroot * lastsquareroot == number:
            lastsquareroot = lastsquareroot - 1
    else:
        lastsquareroot = 1

    #check if prime
    if number > 1:
        for i in range(2, int(number/lastsquareroot)):
            if number % i == 0:
                return False
        return True # returns true for 2 because range(2,2) does not run
    return False

#start timer
starttime = time.time()
primes = []

for i in range(600000):
    if isprime(i, True):
        primes.append(i)

# stop timer
endtime = time.time()
timeelapsed = round(endtime - starttime, 5)

print(len(primes))
print(primes[0])
print(primes[-1])
# print(timeelapsed)
