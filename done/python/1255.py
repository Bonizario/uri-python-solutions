def main():
    from sys import stdin, stdout
    from collections import defaultdict

    for _ in range(int(stdin.readline())):
        d = defaultdict(int)
        s = stdin.readline().strip().lower()
        for c in s:
            if 'a' <= c <= 'z':
                d[c] += 1
        max_ocurr = max(d.values())
        ans = ''.join(letter for (letter, ocurr) in d.items() if ocurr == max_ocurr)
        stdout.write(''.join(sorted(ans)) + '\n')

main()

''' Sorting the whole dict with itemgetter
def main():
    from sys import stdin, stdout
    from collections import defaultdict
    from operator import itemgetter
    n = int(stdin.readline())
    for _ in range(n):
        d = defaultdict(int)
        s = stdin.readline().strip().lower()
        for c in s:
            if 'a' <= c <= 'z':
                d[c] -= 1
        letters = sorted(d.items(), key=itemgetter(1, 0))
        ans = letters[0][0]
        i, size = 1, len(letters)
        while (i < size) and (letters[i][1] == letters[i - 1][1]):
            ans += letters[i][0]
            i += 1
        stdout.write(ans + '\n')
main()
'''
