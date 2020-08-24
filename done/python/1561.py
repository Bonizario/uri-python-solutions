# 1561 - CONVERT DECIMAL INTEGER TO BINARY ARRAY/FORMAT NUMBERS
# def decimal_to_binary_array(decimal):
#     binary_array = ['  ', '  ', '  ', '  ', '  ', '  ']
#     counter = 0
#     while decimal > 0:
#         remainder = decimal % 2
#         decimal = decimal // 2
#         if remainder:
#             binary_array.insert(counter, ' o')
#         else:
#             binary_array.insert(counter, '  ')
#         counter += 1
#     return binary_array

def main():
    from sys import stdin, stdout
    while True:
        try:
            hours, minutes = [int(x) for x in stdin.readline().split(':')]

            h = ['  ', '  ', '  ', '  ', '  ', '  ']
            counter = 0
            while hours > 0:
                remainder = hours % 2
                hours = hours // 2
                if remainder:
                    h.insert(counter, ' o')
                else:
                    h.insert(counter, '  ')
                counter += 1

            m = ['  ', '  ', '  ', '  ', '  ', '  ']
            counter = 0
            while minutes > 0:
                remainder = minutes % 2
                minutes = minutes // 2
                if remainder:
                    m.insert(counter, ' o')
                else:
                    m.insert(counter, '  ')
                counter += 1

            stdout.write(' ____________________________________________\n')
            stdout.write('|                                            |\n')
            stdout.write('|    ____________________________________    |_\n')
            stdout.write('|   |                                    |   |_)\n')
            stdout.write('|   |   8         4         2         1  |   |\n')
            stdout.write('|   |                                    |   |\n')
            stdout.write('|   |  {}        {}        {}        {}  |   |\n'.format(h[3], h[2], h[1], h[0]))
            stdout.write('|   |                                    |   |\n')
            stdout.write('|   |                                    |   |\n')
            stdout.write('|   |  {}    {}    {}    {}    {}    {}  |   |\n'.format(m[5], m[4], m[3], m[2], m[1], m[0]))
            stdout.write('|   |                                    |   |\n')
            stdout.write('|   |   32    16    8     4     2     1  |   |_\n')
            stdout.write('|   |____________________________________|   |_)\n')
            stdout.write('|                                            |\n')
            stdout.write('|____________________________________________|\n\n')
        except Exception:
            break

if __name__ == '__main__':
    main()
