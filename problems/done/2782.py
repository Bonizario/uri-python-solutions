# 2782 - Stepladder
def main():
    from sys import stdin, stdout

    N = int(stdin.readline())
    sequence = [int(s) for s in stdin.readline().split()]
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
        stdout.write(str(stepladders) + '\n')

if __name__ == '__main__':
    main()
