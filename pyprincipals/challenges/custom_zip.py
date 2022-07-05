def zap(a, b):
    return [(a[i], b[i]) for i in range(len(a))]


print(zap([1, 2], [3, 4]))
print(zap([0, 1, 2, 3], [5, 6, 7, 8]))
