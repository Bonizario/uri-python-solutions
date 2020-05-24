# 1847 - Welcome to the Winter!
def main():
    from sys import stdin, stdout
    A, B, C = [int(x) for x in stdin.readline().split()]
    temp1 = B - A
    temp2 = C - B

    if (temp1 < 0) and (temp2 >= 0):
        stdout.write(':)\n')
    elif (temp1 > 0) and (temp2 <= 0):
        stdout.write(':(\n')
    elif (temp1 > 0) and (temp2 > 0) and (temp1 - temp2 > 0):
        stdout.write(':(\n')
    elif (temp1 > 0) and (temp2 > 0) and (temp1 - temp2 <= 0):
        stdout.write(':)\n')
    elif (temp1 < 0) and (temp2 < 0) and (temp1 - temp2 < 0):
        stdout.write(':)\n')
    elif (temp1 < 0) and (temp2 < 0) and (temp1 - temp2 >= 0):
        stdout.write(':(\n')
    elif (temp1 == 0) and (temp2 > 0):
        stdout.write(':)\n')
    elif (temp1 == 0) and (temp2 <= 0):
        stdout.write(':(\n')

if __name__ == '__main__':
    main()
