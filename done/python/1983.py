def main():
    from sys import stdin, stdout

    ok = False
    max_number, max_value = '', 0
    for _ in range(int(stdin.readline())):
        number, value = stdin.readline().split()
        value = float(value)
        if not ok and value >= 8:
            ok = True
        if value > max_value:
            max_number, max_value = number, value
    stdout.write('%s\n' % (max_number if ok else 'Minimum note not reached'))

main()
