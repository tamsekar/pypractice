def positive_numbers(num_list):
    result = []
    for num in num_list:
        if num < 1:
            continue
        result.append(num)
    return result


print(positive_numbers([-10, 10, 20]))
print(positive_numbers([0, 1, 2]))
