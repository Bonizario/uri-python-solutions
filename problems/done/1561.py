# 1561 - Binary Watch
def decimal_to_binary_array(decimal):
    binary_array = ['  ', '  ', '  ', '  ', '  ', '  ']
    counter = 0
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        if remainder:
            binary_array.insert(counter, ' o')
        else:
            binary_array.insert(counter, '  ')
        counter += 1
    return binary_array


while True:
    try:
        hours, minutes = map(int, input().split(':'))
        h = decimal_to_binary_array(hours)
        m = decimal_to_binary_array(minutes)

        print(' ____________________________________________')
        print('|                                            |')
        print('|    ____________________________________    |_')
        print('|   |                                    |   |_)')
        print('|   |   8         4         2         1  |   |')
        print('|   |                                    |   |')
        print('|   |  {}        {}        {}        {}  |   |'.format(h[3], h[2], h[1], h[0]))
        print('|   |                                    |   |')
        print('|   |                                    |   |')
        print('|   |  {}    {}    {}    {}    {}    {}  |   |'.format(m[5], m[4], m[3], m[2], m[1], m[0]))
        print('|   |                                    |   |')
        print('|   |   32    16    8     4     2     1  |   |_')
        print('|   |____________________________________|   |_)')
        print('|                                            |')
        print('|____________________________________________|')
        print()
    except EOFError:
        break
