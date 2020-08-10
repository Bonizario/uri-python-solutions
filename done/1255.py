def main():
    from sys import stdin, stdout
    from collections import defaultdict

    n = int(stdin.readline())
    for _ in range(n):
        d = defaultdict(int)
        s = stdin.readline().strip().lower()
        for c in s:
            if 'a' <= c <= 'z':
                d[c] -= 1

        ans = ''
        max_ocurrences = 1
        for letter, ocurrences in d.items():
            if ocurrences < max_ocurrences:
                ans = letter
                max_ocurrences = ocurrences
            elif ocurrences == max_ocurrences:
                ans += letter

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
