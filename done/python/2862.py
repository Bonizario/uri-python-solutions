def main():
    from sys import stdin, stdout

    for _ in range(int(stdin.readline())):
        stdout.write('Mais de 8000!\n' if int(stdin.readline()) > 8000 else 'Inseto!\n')

main()
