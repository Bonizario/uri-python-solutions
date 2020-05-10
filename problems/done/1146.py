# 1146 - Growing Sequences
def main():
    from sys import stdin, stdout

    X = int(stdin.readline())
    while X != 0:
        nums_list = ''
        for i in range(1, X + 1):
            nums_list += str(i)
            nums_list += ' '

        nums_list = nums_list[:-1]
        stdout.write('%s\n' % nums_list)

        X = int(stdin.readline())

if __name__ == '__main__':
    main()
