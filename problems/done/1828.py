# 1828 - Bazinga!
rules = [
    ['tesoura','papel'],
    ['papel','tesoura'],
    ['papel','pedra'],
    ['pedra','papel'],
    ['pedra','lagarto'],
    ['lagarto','pedra'],
    ['lagarto','Spock'],
    ['Spock','lagarto'],
    ['Spock','tesoura'],
    ['tesoura','Spock'],
    ['tesoura','lagarto'],
    ['lagarto','tesoura'],
    ['lagarto','papel'],
    ['papel','lagarto'],
    ['papel','Spock'],
    ['Spock','papel'],
    ['Spock','pedra'],
    ['pedra','Spock'],
    ['pedra','tesoura'],
    ['tesoura','pedra']
]

for i in range(1, int(input()) + 1):
    turn = input().split()

    if turn[0] == turn[1]:
        print('Caso #{}: De novo!'.format(i))
    else:
        index = rules.index(turn)
        if index % 2 == 0:
            print('Caso #{}: Bazinga!'.format(i))
        else:
            print('Caso #{}: Raj trapaceou!'.format(i))
