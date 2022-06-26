def all_equal(_lst):
    counter = 0
    if not _lst:
        return True

    for i in range(len(_lst)):
        print(f"{_lst[i]},{_lst[i - 1]}")
        while _lst[i] == _lst[i - 1]:
            counter += 1
            return True


print(all_equal([1, 2, 1]))
# print(all_equal([3, 3, 3, 3, 3, 2, 3]))
