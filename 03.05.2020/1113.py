# 1113 - Ascending and Descending
X, Y = map(int, input().split())
while (X != Y):
    floor = min(X, Y)
    top = max(X, Y)
    if (X == floor):
        print("Crescente")
    elif (X != floor):
        print("Decrescente")
    X, Y = map(int, input().split())
