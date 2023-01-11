'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''
from math import sqrt

def check_prime(num):
    flag = False

    if num <= 1:
        return None
    
    for i in range(2, int(sqrt(num))+1):
        if num%i == 0:
            flag = True
            break
    
    if flag == False:
        return True
    else:
        return False

if __name__ == "__main__":
    value = 2000000
    result = 0

    for i in range(1, value+1):
        if check_prime(i):
            result += i
    
    print(result)
