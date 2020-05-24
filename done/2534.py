# 2534 - General Exam
while True:
    try:
        N, Q = map(int, input().split())
        grades = [int(input()) for _ in range(N)]
        positions = [int(input()) for _ in range(Q)]
        grades.sort(reverse=True)
        for position in positions:
            print(grades[position - 1])
    except EOFError:
        break
