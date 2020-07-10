def main():
    from sys import stdin, stdout

    while True:
        n = int(stdin.readline())
        if n == 0:
            break
        loop = list(map(int, stdin.readline().split()))

        # loop with only 2 values special case
        if len(loop) == 2:
            stdout.write('2\n')
            continue

        ascending = True if loop[1] > loop[0] else False
        previous = loop[0]
        ans = 0
        for i in range(1, n):
            if loop[i] > previous and not ascending:
                ans += 1
                ascending = True
            elif loop[i] < previous and ascending:
                ans += 1
                ascending = False
            previous = loop[i]

        # first and last values
        if loop[-1] > loop[0] and ascending:
            ans += 1
        elif loop[-1] < loop[0] and not ascending:
            ans += 1

        # first value being an inflexion point
        if loop[0] < loop[1] and loop[0] < loop[-1]:
            ans += 1
        elif loop[0] > loop[1] and loop[0] > loop[-1]:
            ans += 1

        stdout.write('%d\n' % ans)

main()
