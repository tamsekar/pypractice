colors = ["red", "green", "blue"]
result = 0
# your code goes here
for color1 in colors:
    for color2 in colors:
        if color1 == color2:
            continue
        result = color1 + "-" + color2
        print(result)
