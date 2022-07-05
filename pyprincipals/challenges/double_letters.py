def double_letters(strings):
    result = 0
    for i in range(len(strings) - 1):
        if strings[i + 1] == strings[i]:
            return True
    return False


print(double_letters('Helol'))
