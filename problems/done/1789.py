# 1789 - The slug race
def main():
    from sys import stdin, stdout
    while True:
        try:
            L = int(stdin.readline())
            Vi = [int(v) for v in stdin.readline().split()]
            Vi.sort()
            mais_veloz = Vi[-1]
            if mais_veloz < 10:
                stdout.write('1\n')
            elif mais_veloz >= 10 and mais_veloz < 20:
                stdout.write('2\n')
            else:
                stdout.write('3\n')
        except Exception:
            break

if __name__ == '__main__':
    main()
