def main():
    from sys import stdin, stdout

    hours = [list(map(int, stdin.readline().split())) for _ in range(int(stdin.readline()))]
    ans = '\n'.join(f'{hour[0]:02d}:{hour[1]:02d} - A porta {"abriu" if hour[2] else "fechou"}!' for hour in hours)
    stdout.write(f'{ans}\n')

main()
