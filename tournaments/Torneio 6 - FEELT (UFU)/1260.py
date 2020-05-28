N = int(input())
for i in range(N):
    arvores = dict()
    if i == 0:
        temp = input()

    while True:
        try:
            arvore = input()
            if arvore == '':
                break
        except EOFError:
            break

        if arvore not in arvores.keys():
            arvores[arvore] = 1
        else:
            arvores[arvore] += 1

    total = 0
    for arvore in arvores:
        total += float(arvores[arvore])
    arvores = sorted(arvores.items())

    for arvore in arvores:
        print('{} {:.4f}'.format(arvore[0], arvore[1]/total*100))

    if i != N-1:
        print()
