from math import pi
def radians_to_degrees(a):
    result = a * (180/pi)
    return result

a = 1
print(round(radians_to_degrees(a),3))