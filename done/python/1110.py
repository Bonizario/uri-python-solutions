def main():
    from sys import stdin, stdout
    from collections import deque

    while True:
        n = int(stdin.readline())
        if not n:
            break
        cards = deque(range(1, n + 1))
        discarded = list()
        while len(cards) > 1:
            discarded.append(cards[0])
            cards.popleft()
            cards.append(cards[0])
            cards.popleft()
        stdout.write('Discarded cards: ' + ', '.join([str(disc) for disc in discarded]))
        stdout.write('\nRemaining card: {}\n'.format(cards[0]))
main()
