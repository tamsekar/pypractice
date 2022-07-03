def count(string):
    # your code here
    _dict = {}
    for i in string:
        counter = string.count(i)
        _dict[i] = counter
    return _dict


print(count("hello"))
