def merge(table):
    length = len(table)
    ret_str = ''
    for n in range(length - 1):
        ret_str = ret_str + table[0] + ','

    ret_str = ret_str + 'and' + ' ' + table[length - 1]
    return ret_str

spam = ['apples', 'bananas', 'tofu', 'cats']
print(spam)
new_str = merge(spam)
print(new_str)