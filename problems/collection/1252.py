# 1252 - SORT USING MOD (C/C++ LIKE) AND KEY FUNCTION WITH TERNARY AND BITWISE OPERATORS
def main():
    from sys import stdin, stdout

    while True:
        N, M = [int(x) for x in stdin.readline().split()]
        stdout.write('%d %d\n' % (N, M))
        if N == 0 and M == 0:
            break

        nums = [int(stdin.readline()) for _ in range(N)]
        odds, evens = [], []
        for num in nums:
            if num & 1:
                odds.append(num)
            else:
                evens.append(num)

        nums = sorted(odds, reverse=True) + sorted(evens)
        nums.sort(key=lambda x: (x % M if x >=0 else -(-x % M), not x & 1))

        for num in nums:
            stdout.write(str(num) + '\n')

if __name__ == '__main__':
    main()
