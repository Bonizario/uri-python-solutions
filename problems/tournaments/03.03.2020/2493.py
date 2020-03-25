# 2493 - Jogo do Operador
while True:
    try:
        t = int(input())
        exps = [input() for _ in range(t)]
        ans = [input() for _ in range(t)]

        calcs = []
        for exp in exps:
            calc = [float(exp.split()[0])]
            sec = exp.split()[1].split('=')
            calc += [float(s) for s in sec]
            calcs.append(calc)

        players = []
        losers = []
        for a in ans:
            player, i, op = a.split()
            players.append(player)
            calc = calcs[int(i)-1]
            if op == '+':
                if calc[0] + calc[1] != calc[2]:
                    losers.append(player)
            elif op == '-':
                if calc[0] - calc[1] != calc[2]:
                    losers.append(player)
            elif op == '*':
                if calc[0] * calc[1] != calc[2]:
                    losers.append(player)
            elif op == 'I':
                if calc[0] + calc[1] == calc[2]:
                    losers.append(player)
                elif calc[0] - calc[1] == calc[2]:
                    losers.append(player)
                elif calc[0] * calc[1] == calc[2]:
                    losers.append(player)
        if all(player in losers for player in players):
            print('None Shall Pass!')
        elif len(losers) == 0:
            print('You Shall All Pass!')
        else:
            losers.sort()
            print(' '.join(losers))
    except EOFError:
        break
