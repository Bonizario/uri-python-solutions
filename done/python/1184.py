def main():
    from sys import stdin, stdout
    result = 0
    operation = stdin.readline().strip()
    for i in range(12):
        for j in range(12):
            tmp = float(stdin.readline())
            if i > j:
                result += tmp
    stdout.write('{:.1f}\n'.format(result if operation == 'S' else result / 66.0))
main()
