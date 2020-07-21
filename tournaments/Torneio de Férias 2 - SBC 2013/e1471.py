def main():
    from sys import stdin, stdout

    while True:
        try:
            n, r = map(int, stdin.readline().split())
            voltaram = tuple(map(int, stdin.readline().split()))
        except Exception:
            break

        if n == r:
            stdout.write('*\n')
        else:
            mergulhadores = {i: i for i in range(1, n + 1)}
            for n in voltaram:
                mergulhadores[n] = 0
            stdout.write(' '.join(str(i) for i in mergulhadores if mergulhadores[i]) + ' \n')
main()
