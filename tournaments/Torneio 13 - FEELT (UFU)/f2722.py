def main():
    from sys import stdin, stdout
    n = int(stdin.readline())
    for _ in range(n):
        s1 = stdin.readline().strip()
        s2 = stdin.readline().strip()
        t1 = len(s1)
        t2 = len(s2)
        if t1 > t2:
            s2 += ' ' * (t1 - t2)
        elif t1 < t2:
            s1 += ' ' * (t2 - t1)
        ans = ''
        for i in range(0, t1, 2):
            ans += s1[i:i+2]
            ans += s2[i:i+2]
        stdout.write(ans.strip() + '\n')
main()
