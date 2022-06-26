def consecutive_zeros(string):
    _count_list = []
    counter = 0
    for i in range(len(string)):
        _count_list.append(string[i])
        if _count_list[i] == "0":
            if _count_list[i] == _count_list[i - 1]:
                counter += 1
            elif _count_list == "1":
                counter = 0
    return counter


print(consecutive_zeros("10101"))
