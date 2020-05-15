# 1120 - DELETE EXTRAS ZEROS (LEFT) AND BROKEN NUMBER FROM STRING
def main():
    from sys import stdin, stdout

    while True:
        broken, numbers = stdin.readline().split()
        if broken == '0' and numbers == '0':
            break

        try:
            numbers = numbers.replace(broken, '')
        except Exception:
            pass

        start = 0
        empty = True
        for i in range(len(numbers)):
            if numbers[i] != '0':
                start = i
                empty = False
                break
        if not empty:
            numbers = numbers[start:]
            stdout.write('%s\n' % numbers)
        else:
            stdout.write('0\n')

if __name__ == '__main__':
    main()
