# 2033 - Interest on Loan
def main():
    from sys import stdin, stdout

    while True:
        try:
            C = float(stdin.readline())
            i = float(stdin.readline())
            n = int(stdin.readline())
        except Exception:
            break

        juros_simples = C * i * n
        juros_composto = C * (1 + i)**n - C
        simples = abs(C - (C + juros_simples)) # python weird behavior
        composto = abs(C - (C + juros_composto)) # 100% WA without these 2 lines
        diferenca_valor = abs(juros_simples - juros_composto)
        stdout.write('DIFERENCA DE VALOR = %.2f\n' % diferenca_valor)
        stdout.write('JUROS SIMPLES = %.2f\n' % simples)
        stdout.write('JUROS COMPOSTO = %.2f\n' % composto)

if __name__ == '__main__':
    main()
