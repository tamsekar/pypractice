def flatten(lst):
    result = []
    for x in lst:
        for y in x:
            if y not in result:
                result.append(y)
    return result


print(flatten([[1, 2], [3, 4]]))
