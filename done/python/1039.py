# 1039 - Fire Flowers
def main():
    from sys import stdin, stdout
    from math import sqrt
    while True:
        try:
            R1, X1, Y1, R2, X2, Y2 = [int(x) for x in stdin.readline().split()]
            if (R1 < R2):
                stdout.write("MORTO\n")
            else:
                rich = (R1-R2) >= sqrt((X2-X1)*(X2-X1) + (Y2-Y1)*(Y2-Y1))
                if rich:
                    stdout.write("RICO\n")
                else:
                    stdout.write("MORTO\n")
        except:
            break

if __name__ == '__main__':
    main()
