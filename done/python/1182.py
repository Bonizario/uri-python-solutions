def main():
    from sys import stdin, stdout
    result = 0
    column = int(stdin.readline())
    operation = stdin.readline().strip()
    for i in range(12):
        for j in range(12):
            tmp = float(stdin.readline())
            if j == column:
                result += tmp
    stdout.write('{:.1f}\n'.format(result if operation == 'S' else result / 12.0))
main()
