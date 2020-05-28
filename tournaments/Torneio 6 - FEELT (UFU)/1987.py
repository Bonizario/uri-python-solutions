while True:
    try:
        n, m = input().split()

    except EOFError:
        break
    n = int(n)

    total = 0
    for i in range(n):
        total += int(m[i])
    if total % 3 == 0:
        print('{} sim'.format(total))
    else:
        print('{} nao'.format(total))
