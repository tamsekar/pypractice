def unique(string):
    result = ""
    for i in string:
        if i not in result:
            result = result + i
    return result


print(unique("abc"))
print(unique("aa"))
print(unique("xxyyxxzz"))
print(unique("hello"))