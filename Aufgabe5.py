'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Need time to solve the problem, because of the large number.
'''

if __name__ == "__main__":
    start = 1
    max_num = 20
    result = ""

    while True:
        for i in range(1, max_num+1):
            if start%i != 0:
                break

            if i == max_num and start %i == 0:
                result = start
                break
        
        if result:
            break

        start += 1

    print(result)
        