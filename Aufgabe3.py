'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from math import sqrt

if __name__ == "__main__":
    num = 600851475143
    prime_num = []

    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            prime_num.append(i)
    
    result = [i for i in prime_num if any(x for x in prime_num if i%x ==0 and x != i) == False]
    print(result)