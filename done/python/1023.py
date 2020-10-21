def main():
    from sys import stdin, stdout
    from collections import defaultdict
    from operator import itemgetter
    from math import floor

    def truncate(f):
        return floor(f * 100) / 100

    city = 1
    n = int(stdin.readline())
    while True:
        consumptions = defaultdict(int)
        total_consumption = total_residents = 0
        for _ in range(n):
            x, y = map(int, stdin.readline().split())
            consumptions[y // x] += x
            total_consumption += y
            total_residents += x

        stdout.write(f'Cidade# {city}:\n')
        stdout.write(' '.join(f'{c[1]}-{c[0]}' for c in sorted(consumptions.items(), key=itemgetter(0))))
        stdout.write(f'\nConsumo medio: {truncate(total_consumption / total_residents):.2f} m3.\n')

        n = int(stdin.readline())
        if n == 0:
            break
        stdout.write('\n')
        city += 1

main()
