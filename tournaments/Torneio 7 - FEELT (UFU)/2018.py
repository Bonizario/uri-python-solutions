# 2018 - Christmas Olympics
print('Quadro de Medalhas')
medalhas = dict()
while True:
    try:
        jogo = input()
    except EOFError:
        break

    primeiro = input()
    segundo = input()
    terceiro = input()

    if primeiro not in medalhas:
        medalhas[primeiro] = [-1, 0, 0]
    else:
        medalhas[primeiro][0] -= 1

    if segundo not in medalhas:
        medalhas[segundo] = [0, -1, 0]
    else:
        medalhas[segundo][1] -= 1

    if terceiro not in medalhas:
        medalhas[terceiro] = [0, 0, -1]
    else:
        medalhas[terceiro][2] -= 1

medalhas = sorted(medalhas.items(), key=lambda x: (x[1], x[0]))
# print(medalhas)
for pais in medalhas:
    print('{} {} {} {}'.format(pais[0], -1 *
                               pais[1][0], -1*pais[1][1], -1*pais[1][2]))
