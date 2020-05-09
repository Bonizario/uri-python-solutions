# 1769 - SSN 1 (CPF)
def main():
    from sys import stdin, stdout

    while True:
        try:
            entry, digits = stdin.readline().split('-')
        except Exception:
            break
        entry = entry.replace('.', '')
        aux1 = 0
        aux2 = 0
        for i in range(len(entry)):
            aux1 += int(entry[i])*(i + 1)
            aux2 += int(entry[i])*(9 - i)
        b1 = aux1 % 11
        b2 = aux2 % 11
        if b1 == 10:
            b1 = 0
        if b2 == 10:
            b2 = 0
        if digits[0] == str(b1) and digits[1] == str(b2):
            stdout.write('CPF valido\n')
        else:
            stdout.write('CPF invalido\n')
if __name__ == '__main__':
    main()
