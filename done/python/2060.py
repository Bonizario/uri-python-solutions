# 2060 - Desafio de Bino
def main():
    from sys import stdin, stdout

    n = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))
    m2 = m3 = m4 = m5 = 0
    for num in nums:
        if num % 2 == 0:
            m2 += 1
        if num % 3 == 0:
            m3 += 1
        if num % 4 == 0:
            m4 += 1
        if num % 5 == 0:
            m5 += 1
    stdout.write('%d Multiplo(s) de 2\n%d Multiplo(s) de 3\n%d Multiplo(s) de 4\n%d Multiplo(s) de 5\n' % (m2, m3, m4, m5))

main()
