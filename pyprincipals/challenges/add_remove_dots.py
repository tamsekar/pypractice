def add_dots(string):
    return ".".join(string)


def remove_dots(string):
    return string.replace(".", "")


print(add_dots("Hello"))
print(remove_dots("Hello"))