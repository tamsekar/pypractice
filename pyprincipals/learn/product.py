def product(num_list):
    prod_ = 1
    for num in num_list:
        prod_ = prod_ * num
    return prod_


print(product([1, 2, 3, 4]))
print(product([3, 3, 3]))
print(product([2, 2]))
print(product([1, 1]))
