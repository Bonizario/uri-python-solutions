# 1035 - Selection Test 1
def main():
    from sys import stdin, stdout
    A, B, C, D = [int(x) for x in stdin.readline().split()]
    if (B > C) and (D > A) and (C+D > A+B) and (C > 0) and (D > 0) and (A % 2 ==0):
        stdout.write('Valores aceitos\n')
    else:
        stdout.write('Valores nao aceitos\n')

if __name__ == '__main__':
    main()
