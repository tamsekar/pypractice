def list_xor(n, list1, list2):
    if n not in list1 and n not in list2:
        return False
    if n in list1 and n in list2:
        return False
    return True


# solution2 with operator ^
# ^ 	XOR 	Sets each bit to 1 if only one of two bits is 1
# https://www.w3schools.com/python/python_operators.asp

def list_xor1(n, list1, list2):
    return (n in list1) ^ (n in list2)


print(f"Testcase1: {list_xor(1, [0, 2, 3], [1, 5, 6])}")  # == True
print(f"Testcase2: {list_xor(1, [1, 2, 3], [4, 5, 6])}")  # == True
print(f"Testcase3: {list_xor(1, [1, 2, 3], [1, 5, 6])}")  # == False
print(f"Testcase4: {list_xor(1, [0, 0, 0], [4, 5, 6])}")  # == False
