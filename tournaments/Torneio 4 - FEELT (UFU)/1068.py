# 1068 - Parenthesis Balance I
while True:
    try:
        expression = input()
    except EOFError:
        break
    aux = 0
    for e in expression:
        if e == '(':
            aux += 1
        elif e == ')':
            aux -= 1
            if aux < 0:
                break
    if aux == 0:
        print('correct')
    else:
        print('incorrect')
