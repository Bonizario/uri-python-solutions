# 1257 - Array Hash
def main():
    from sys import stdin, stdout
    for _ in range(int(stdin.readline())):
        N = int(stdin.readline())
        value = 0
        for i in range(N):
            text = stdin.readline().rstrip()
            aux = 0
            for j in range(len(text)):
                aux += i + j
                aux += ord(text[j]) - 65
            value += aux
        stdout.write('%s\n' % value)
if __name__ == '__main__':
    main()