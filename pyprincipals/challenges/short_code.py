def convert(lt):
    return [str(x) for x in lt]


# solution 2
def convert1(ns):
    return list(map(str, ns))


print(convert([1, 2, 3]))
print(convert1([1, 2, 3]))
