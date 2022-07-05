def largest_difference(_list):
    sorted_list = sorted(_list, reverse=True)
    print(sorted_list)
    return sorted_list[0] - sorted_list[-1]


print(largest_difference([1, 2, 3, 5, 6]))
