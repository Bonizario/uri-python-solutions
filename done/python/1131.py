# 1131 - Grenais
grenal = 1
scoreboard = [0, 0, 0]

while grenal != 2:
    inter, gremio = map(int, input().split())
    if inter > gremio:
        scoreboard[0] += 1
    elif gremio > inter:
        scoreboard[1] += 1
    elif gremio == inter:
        scoreboard[2] += 1
    grenal = int(input('Novo grenal (1-sim 2-nao)\n'))

print('{} grenais'.format(sum(scoreboard)))
print('Inter:{}'.format(scoreboard[0]))
print('Gremio:{}'.format(scoreboard[1]))
print('Empates:{}'.format(scoreboard[2]))

if scoreboard[0] > scoreboard[1]:
    print('Inter venceu mais')
elif scoreboard[0] < scoreboard[1]:
    print('Gremio venceu mais')
else:
    print('Não houve vencedor')
