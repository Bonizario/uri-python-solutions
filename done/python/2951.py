def main():
    from sys import stdin, stdout

    runes = {}
    n, g = map(int, stdin.readline().split())
    for _ in range(n):
        rune, power = stdin.readline().split()
        runes[rune] = int(power)

    stdin.readline()
    friendship = sum(runes[rune] for rune in stdin.readline().split())
    stdout.write('%d\n' % friendship)
    stdout.write('%s\n' % ('You shall pass!' if friendship >= g else 'My precioooous'))

main()
