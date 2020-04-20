# 1192 - Paula's Mathematic Game
n = int(input())
for _ in range(n):
    entries = input()
    n1, letter, n2 = int(entries[0]), entries[1], int(entries[2])

    if n1 == n2:
        print(n1 * n2)
    elif letter >= 'A' and letter <= 'Z':
        print(n2 - n1)
    elif letter >= 'a' and letter <= 'z':
        print(n1 + n2)
