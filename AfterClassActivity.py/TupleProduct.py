def product_of_tuple(tup):
    product = 1
    for num in tup:
        product *= num
    return product

tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

print("The product of tup1 is:", product_of_tuple(tup1))
print("The product of tup2 is:", product_of_tuple(tup2))