def collatz(num):
    ret = 0
    if ((num % 2) == 0):
        ret = num // 2
    else:
        ret = 3 * num + 1
    print('The number is ' + str(ret))

    return ret

global number
print('Please input a integer.')
m = 0
while (m == 0):
    try:
        number = int(input())
        m = 1
    except ValueError:
        print('Error: Please input a integer! ')
        m = 0

number = collatz(number)
while  (number != 1):
    number = collatz(number)
