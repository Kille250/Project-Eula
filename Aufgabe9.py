'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
from math import sqrt


'''
a+b+c=1000
b+c= 1000-a
c=1000-a-b

a+b+c=1000
a+b-1000 =-c
a-b+1000=c
'''
if __name__ == "__main__":
    value = 1000
    result = 0

    for a in range(1, value):
        for b in range(1, value):
            c = -a-b+1000
            if (a**2+b**2 == c**2):
                result = a*b*c
    
    print(result)
