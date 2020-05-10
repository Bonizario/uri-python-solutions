# 1124 - Elevador
def main():
    from sys import stdin, stdout
    from math import sqrt

    while True:
        values = stdin.readline().rstrip()
        if values == '0 0 0 0':
            break

        L, C, R1, R2 = [int(x) for x in values.split()]

        X2, Y2 = C - R2, L - R2
        distance = sqrt((X2-R1)*(X2-R1) + (Y2-R1)*(Y2-R1))

        if distance >= (R1 + R2):
            if (2*R1 <= C) and (2*R1 <= L) and (2*R2 <= C) and (2*R2 <= L):
                stdout.write("S\n")
            else:
                stdout.write("N\n")
        else:
            stdout.write("N\n")

if __name__ == '__main__':
    main()
