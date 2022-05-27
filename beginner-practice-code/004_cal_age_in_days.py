def calc_age(age):
    result = age * 365
    return result

print("Enter your age: ")
age = int(input())
print("Your age in days: ", calc_age(age))