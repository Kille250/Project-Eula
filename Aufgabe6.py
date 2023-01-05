'''
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is:

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

if __name__ == "__main__":
    max_num = 100
    sum_square_of_numb = 0
    sum_square_of_sum = 0
    result = ""

    for i in range(1, max_num+1):
        sum_square_of_numb += i**2

        sum_square_of_sum += i

    sum_square_of_sum = sum_square_of_sum**2

    result = sum_square_of_sum - sum_square_of_numb
    
    print(result)