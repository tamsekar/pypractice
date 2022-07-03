def is_uppercase(letter):
    return letter.isupper()


def initials(s):
    result = ""
    for i in s:
        if is_uppercase(i):
            result = result + i
    return result


print(initials("John Doe"))
