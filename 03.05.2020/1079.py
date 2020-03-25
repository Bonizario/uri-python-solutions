# 1079 - Weighted Averages
N = int(input())
for _ in range(N):
    n1, n2, n3 = map(float, input().split())
    weighted_average = (n1 * 2 + n2 * 3 + n3 * 5) / 10
    print("{:.1f}".format(weighted_average))
