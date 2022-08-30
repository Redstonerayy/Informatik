#simple function
from curses.ascii import isprint


def isprime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False

        return True
    return False

i = int(input())
print(isprime(i))
