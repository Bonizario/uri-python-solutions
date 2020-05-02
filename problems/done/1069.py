# 1069 - Diamonds and Sand
for _ in range(int(input())):
    diamonds = input()
    aux = 0
    counter = 0
    for d in diamonds:
        if d == '<':
            aux += 1
        elif d == '>':
            if aux > 0:
                aux -= 1
                counter += 1
    print(counter)
