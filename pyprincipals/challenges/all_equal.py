def all_equal(_lst):
    return _lst[:-1] == _lst[1:]


print(all_equal([1, 2, 3]))
print(all_equal([3, 3, 3, 3, 3, 2, 3]))
