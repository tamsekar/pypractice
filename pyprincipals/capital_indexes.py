def capital_indexes(s):
    idx_list = []
    idx_pos = 0

    for i in s:
        if i.isupper():
            idx_pos = s.index(i, idx_pos)
            idx_list.append(idx_pos)
            idx_pos += 1
            print(idx_list)
    return idx_list


capital_indexes('HIhHShcOOl')
