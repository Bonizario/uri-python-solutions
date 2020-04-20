# 2782 - Stepladder
N = int(input())
sequence = [int(s) for s in input().split()]
if N == 1 or N == 2:
    print(1)
else:
    stepladders = 1
    before = sequence[0] - sequence[1]
    for i in range(2, N):
        now = sequence[i - 1] - sequence[i]
        if now != before: # changing the pattern
            before = now
            stepladders += 1
    print(stepladders)
