def equal_coordinates(coords):
    result = []
    for c in coords:
        x, y = c
        if x == y:
            result.append(c)
    return result


print(equal_coordinates([(1, 2), (2, 2), (3, 2)]))
