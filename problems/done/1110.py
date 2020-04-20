# 1110 - Throwing Cards Away
while True:
    n = int(input())
    if not n:
        break
    cards = [card for card in range(1, n + 1)]
    discarded = []
    while len(cards) > 1:
        discarded.append(cards[0])
        cards.pop(0)
        cards.append(cards[0])
        cards.pop(0)

    print('Discarded cards: ' + ', '.join([str(disc) for disc in discarded]))
    print('Remaining card: {}'.format(cards[0]))
