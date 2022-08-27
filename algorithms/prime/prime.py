#simple function
def isprime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False

        return True
    return False

for i in range(20):
    if isprime(i):
        print(i)