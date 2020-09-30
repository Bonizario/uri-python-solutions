def main():
    from sys import stdin, stdout
    n = int(stdin.readline())

    for _ in range(n):
        m = int(stdin.readline())

        students = list(map(int, stdin.readline().split()))
        ordered = sorted(students, reverse=True)

        not_changed = 0
        for i in range(m):
            if students[i] == ordered[i]:
                not_changed += 1

        stdout.write(f'{not_changed}\n')
main()
