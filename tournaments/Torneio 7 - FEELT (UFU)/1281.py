# 1281 - Going to the Market
for _ in range(int(input())):
    produtos = dict()
    total = 0

    for _ in range(int(input())):
        nome, preco = input().split()
        produtos[nome] = float(preco)

    for _ in range(int(input())):
        nome, quantidade = input().split()
        quantidade = int(quantidade)
        total += produtos[nome] * quantidade

    print('R$ {:.2f}'.format(total))
