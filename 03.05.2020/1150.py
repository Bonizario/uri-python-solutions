# 1150 - Exceeding Z
X = int(input())
Z = int(input())
increment = X + 1
counter = 1
while Z <= X:
    Z = int(input())
while X < Z:
    X += increment
    increment += 1
    counter += 1
print(counter)
