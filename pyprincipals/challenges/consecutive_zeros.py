# Solution 1
def consecutive_zeros(string):
    zeros = []
    length = []

    for i in string:
        if "1" not in string and len(string) == 1:
            return 1

        if i == "0":
            zeros.append(i)
        else:
            length.append(len(zeros))
            zeros.clear()
    return max(length)


# Solution 2
def consecutive_zeros2(bin_str):
    result = 0
    streak = 0
    for letter in bin_str:
        if letter == "0":
            streak += 1
        else:
            streak = 0
        result = max(result, streak)
    return result


# Solution 3
def consecutive_zeros3(string):
    return max([len(s) for s in string.split("1")])


print(consecutive_zeros("0"))
print(consecutive_zeros("101"))
print(consecutive_zeros("1010"))
print(consecutive_zeros("1001101000110"))
print(consecutive_zeros("00000"))

print(consecutive_zeros2("0"))
print(consecutive_zeros2("101"))
print(consecutive_zeros2("1010"))
print(consecutive_zeros2("1001101000110"))
print(consecutive_zeros2("00000"))

print(consecutive_zeros3("0"))
print(consecutive_zeros3("101"))
print(consecutive_zeros3("1010"))
print(consecutive_zeros3("1001101000110"))
print(consecutive_zeros3("00000"))
