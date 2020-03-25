# 2813 - Avoiding Rain
n = int(input())
prevs = [input().split() for _ in range(n)]
now_umb = [0, 0]
total_umb = [0, 0]
for day in prevs:
    for i, state in enumerate(day):
        if state == 'chuva':
            if now_umb[i] == 0:
                now_umb[i] += 1
                total_umb[i] += 1
            now_umb[i] -= 1
            now_umb[1 - i] += 1
print(' '.join(map(str, total_umb)))
