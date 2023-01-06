'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from math import sqrt

if __name__ == "__main__":
    start_num = 2
    max_prime_number = 10001
    prime_list = []

    while len(prime_list) < max_prime_number:
        
        if any([i for i in prime_list if start_num%i == 0 and start_num != i]) is False:
            prime_list.append(start_num)

        start_num += 1

    print(prime_list)
    