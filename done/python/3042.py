def main():
    from sys import stdin, stdout

    while True:
        M = int(stdin.readline())
        if M == 0:
            break
        touches = 0
        santa = [0, 1, 0]
        for _ in range(M):
            line = tuple(map(int, stdin.readline().split()))
            if sum(line) == 2:
                path = line.index(0)
                curr_path = santa.index(1)
                touches += abs(curr_path - path)
                santa[curr_path] = 0;
                santa[path] = 1
        stdout.write('%d\n' % touches)

main()
