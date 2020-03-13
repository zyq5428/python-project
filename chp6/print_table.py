table_data = [
['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']
]

def print_before(table):
    for i in range(len(table)):
        print(table[i])

def print_table(table):
    col_widths = [0] * len(table)
    for m in range(len(table)):
        max = 0
        for n in range(len(table[m])):
            if max < len(table[m][n]):
                max = len(table[m][n])
        col_widths[m] = max

    print(col_widths)
    max_max = 0
    for n in range(len(col_widths)):
        if max_max < col_widths[n]:
                max_max = col_widths[n]

    return max_max

def print_after(table, max):
    for m in range(len(table)):
        for n in range(len(table[m])):
            print(table[m][n].rjust(max), end=' ')
        print('\n')

print_before(table_data)
max = print_table(table_data)
print(str(max))
print_after(table_data, max)