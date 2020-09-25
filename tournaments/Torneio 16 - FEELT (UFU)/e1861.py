def main():
    from sys import stdin, stdout
    from collections import defaultdict
    from operator import itemgetter

    murders = defaultdict(int)
    murdered = set()
    while True:
        try:
            murderer, victim = stdin.readline().strip().split()
        except Exception:
            break
        murders[murderer] += 1
        murdered.add(victim)

    stdout.write('HALL OF MURDERERS\n')

    hall = sorted(murders.items(), key=itemgetter(0))
    for name, kills in hall:
        if name not in murdered:
            stdout.write(f'{name} {kills}\n')

main()
