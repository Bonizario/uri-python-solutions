# 2916 - The Note
def main():
    from sys import stdin, stdout

    mod = 1000000007
    while True:
        try:
            entries = stdin.readline().split()
            N = int(entries[0])
            while len(entries) <= N + 1:
                entries += stdin.readline().split()
            K = int(entries[1])
            notes = [int(x) for x in entries[2:]]
        except Exception:
            break

        notes.sort(reverse=True)
        result = 0
        for i in range(K):
            result += notes[i]
        result %= mod
        stdout.write('%d\n' % result)

if __name__ == '__main__':
    main()
