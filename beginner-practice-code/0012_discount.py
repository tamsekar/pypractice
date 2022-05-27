def discount(price, off):
    result = price * (off/100)
    return result

price = 110
off = 75
print(round(discount(price, off),2))