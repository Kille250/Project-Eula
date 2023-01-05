'''

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

if __name__ == '__main__':
    result = 0
    range_number = 1000
    numb_arr = range(0, range_number)

    for i in numb_arr:
        if i%3 == 0 or i%5 == 0:
            result +=i

    print(str(result))