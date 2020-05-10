# 1238 - Combiner
def main():
    from sys import stdin, stdout

    for _ in range(int(stdin.readline())):
        s1, s2 = stdin.readline().rstrip().split()
        combined = ''
        size1 = len(s1)
        size2 = len(s2)

        if size1 <= size2:
            for i in range(size1):
                combined += s1[i]
                combined += s2[i]
            combined += s2[i+1:]
        else:
            for i in range(size2):
                combined += s1[i]
                combined += s2[i]
            combined += s1[i+1:]

        stdout.write('%s\n' % combined)

if __name__ == '__main__':
    main()
