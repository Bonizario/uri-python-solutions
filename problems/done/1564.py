# 1564 - Brazil World Cup
while True:
    try:
        cup = int(input())
        if not cup:
            print('vai ter copa!')
        else:
            print('vai ter duas!')
    except EOFError:
        break
