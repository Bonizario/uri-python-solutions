# 1252 - Sort! Sort!! And Sort!!!
def main():
    from sys import stdin

    keynum = lambda num: (abs(num)%M * (1 if num>=0 else -1), -1*(num&1), num * (-1 if num&1 else 1))

    while True:
        entry = input()
        print(entry)
        if entry == '0 0':
            break

        N, M = [int(x) for x in entry.split()]
        nums = [int(stdin.readline()) for _ in range(N)]
        nums.sort(key=keynum)
        print('\n'.join(map(str, nums)))

if __name__ == '__main__':
    main()
