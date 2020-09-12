def main():
    from sys import stdin, stdout

    a, b, c = map(int, stdin.readline().split())
    if a >= b + c or b >= a + c or c >= a + b:
        stdout.write('Invalido\n')
        return
    rectangle = a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b
    if a == b == c:
        stdout.write('Valido-Equilatero\n')
    elif a == b or a == c or b == c:
        stdout.write('Valido-Isoceles\n')
    else:
        stdout.write('Valido-Escaleno\n')
    stdout.write(f'Retangulo: {"S" if rectangle else "N"}\n')
main()
