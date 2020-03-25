# 1115 - Quadrant
X, Y = map(int, input().split())
while (X != 0) and (Y != 0):
    if (X > 0) and (Y > 0):
        print("primeiro")
    elif (X < 0) and (Y > 0):
        print("segundo")
    elif (X < 0) and (Y < 0):
        print("terceiro")
    elif (X > 0) and (Y < 0):
        print("quarto")
    X, Y = map(int, input().split())
