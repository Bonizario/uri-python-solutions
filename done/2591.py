# 2591 - HameKameKa
def main():
    from re import search
    from sys import stdin, stdout

    for _ in range(int(stdin.readline())):
        attack = stdin.readline().rstrip()
        filtered = search(r'h([a]*)mek([a]*)me', attack)
        a1 = filtered.group(1)
        a2 = filtered.group(2)
        total = len(a1) * len(a2)
        stdout.write('k%s\n' % ('a'*total))

main()
