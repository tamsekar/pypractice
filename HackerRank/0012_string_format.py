def print_formatted(number):
    # your code goes here
    for i in range(1, n+1):
        p = n.bit_length()
        print(f'{i:{p}d} {i:{p}o} {i:{p}X} {i:{p}b}')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)