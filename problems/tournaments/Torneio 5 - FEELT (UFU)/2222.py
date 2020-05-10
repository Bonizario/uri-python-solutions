# 2222 - Playing with Sets
def main():
    from sys import stdin, stdout
    for _ in range(int(stdin.readline())):
        sets = []
        for _ in range(int(stdin.readline())):
            size, *nums = [int(k) for k in stdin.readline().split()]
            nums = set(nums)
            sets.append(tuple((size, nums)))

        for _ in range(int(stdin.readline())):
            op, X, Y = [int(k) for k in stdin.readline().split()]

            # X and Y are tuples: (size, [nums])
            if op == 1:
                result = sets[X-1][1].intersection(sets[Y-1][1])
            else:
                result = sets[X-1][1].union(sets[Y-1][1])

            stdout.write(str(len(result)) + '\n')
if __name__ == '__main__':
    main()
