def main():
    from sys import stdin, stdout

    n, m = map(int, stdin.readline().split())
    A = [stdin.readline().split() for _ in range(n)]
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if (A[i][j]=='42') and ('7'==A[i-1][j-1]==A[i-1][j]==A[i-1][j+1]==A[i][j-1]==A[i][j+1]==A[i+1][j-1]==A[i+1][j]==A[i+1][j+1]):
               stdout.write(f'{i + 1} {j + 1}\n')
               return
    stdout.write('0 0\n')

main()
