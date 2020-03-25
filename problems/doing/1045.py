# 1045 - Triangle Types
def main():
    from sys import stdin, stdout
    lengths = [float(x) for x in stdin.readline().split()]
    lengths.sort()

    A = lengths[2]
    B = lengths[1]
    C = lengths[0]

    not_triangle = A >= B + C
    temp = B*B + C*C

    if not_triangle:
        stdout.write('NAO FORMA TRIANGULO\n')
    elif (A*A == temp):
        stdout.write('TRIANGULO RETANGULO\n')
    elif (A*A > temp):
        stdout.write('TRIANGULO OBTUSANGULO\n')
    elif (A*A < temp):
        stdout.write('TRIANGULO ACUTANGULO\n')
    if (A == B == C):
        stdout.write('TRIANGULO EQUILATERO\n')
    if ((A == B != C) or (B == C != A) or (C == A != B)) and not not_triangle:
        stdout.write('TRIANGULO ISOSCELES\n')

if __name__ == '__main__':
    main()
