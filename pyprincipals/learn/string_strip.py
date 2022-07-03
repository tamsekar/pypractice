def needs_cleanup(string):
    # your code here
    if string != string.strip():
        return True
    return False


print(needs_cleanup("hello"))
