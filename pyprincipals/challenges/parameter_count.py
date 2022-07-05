def param_count(*args):
    count = 0
    for arg in args:
        count += 1
        if arg == "":
            return 0
    return count


# solution2
def param_count2(*args):
    return len(args)


print(f"Testcase1: {param_count()}")
print(f"Testcase1: {param_count2()}")