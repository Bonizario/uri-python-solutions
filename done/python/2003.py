def main():
    from sys import stdin, stdout

    while True:
        try:
            hours, minutes = map(int, stdin.readline().strip().split(':'))
        except Exception:
            break
        late = hours * 60 + minutes - 420
        stdout.write('Atraso maximo: %d\n' % (late if late > 0 else 0))

main()
