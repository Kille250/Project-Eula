'''

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

1. Die länge muss geprüft werden von der Zahl.
2. Es wird spiegelverkehrt der Anfang mit dem Ende verglichen
'''

begin_num = 100
end_num = 999
all_prod = []

for i in range(begin_num, end_num):
    for x in range(begin_num, end_num):
        split_part = ""
        product = i*x
        product_stringify = str(product)
        split_length = int(len(product_stringify)/2)

        if len(product_stringify) % 2 == 0:
            split_part = product_stringify[:split_length]
        else:
            split_part = product_stringify[:round(split_length)]

        reverse_part = split_part[::-1]

        if product_stringify.startswith(split_part) and product_stringify.endswith(reverse_part):
            all_prod.append(product)

all_prod.sort()

print(all_prod)



        
