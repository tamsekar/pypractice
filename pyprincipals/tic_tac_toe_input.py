def get_row_col(choice):
    translate = {"A": 0, "B": 1, "C": 2}
    letter = choice[0]
    print(f"Debug: {letter}")
    number = choice[1]
    print(f"Debug: {number}")
    row = int(number) - 1
    print(f"Debug: {row}")
    column = translate[letter]
    print(f"Debug: {column}")
    return row, column


print(get_row_col("A3"))
