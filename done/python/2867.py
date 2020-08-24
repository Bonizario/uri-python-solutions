# 2867 - LENGTH OF LOOONG INTEGERS
def main():
    from sys import stdin, stdout
    from math import log10 # (inaccurate for extremely long lengths, use len(str))

    C = int(stdin.readline())
    for _ in range(C):
        N, M = [int(x) for x in stdin.readline().split()]
        result = N**M # (1 <= N, M <= 100)
        digits = int(log10(result)) + 1
        stdout.write(str(digits) + '\n')

if __name__ == '__main__':
    main()
