import sys


def read_file(filename):
    f = open(filename, 'r')
    return f


print(read_file('/tmp/small.txt'))


# sys.exit(0)


def print_words(filename):
    word_list = []
    word_dict = {}
    count = 0

    for line in read_file(filename):
        word_list.append(line.strip())
        # print("First For: ", word_list)

    for i in range(len(word_list)):
        word_list[i] = word_list[i].lower()
        # print("Second For: ", word_list)
        for line in word_list:
            word_list[i].split()
    strings = ' '.join(word_list)
    # print(strings)
    str_list = strings.split()

    for substr in str_list:
        #  print('Substring: ', substr)
        count = strings.count(substr)
        word_dict[substr] = count
    #  print(word_dict)
    return word_dict


def print_top(filename):
    pwf = print_words(filename)
    sorted_dict = {}

    sorted_list = sorted(pwf.values(), reverse=True)

    for skey in sorted_list:
        for key, value in pwf.items():
            if value == skey:
                sorted_dict[key] = value
    print(sorted_dict)
    return sorted_dict


# print_words('/tmp/small.txt')
print_top('/tmp/small.txt')
