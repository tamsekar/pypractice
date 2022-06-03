mark_sheet = []
for _ in range(0, int(input())):
    mark_sheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in mark_sheet])))[1]
print('\n'.join([a for a, b in sorted(mark_sheet) if b == second_highest]))