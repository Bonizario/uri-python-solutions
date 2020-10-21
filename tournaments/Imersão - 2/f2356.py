def main():
    while True:
        try:
            d = input().strip()
            s = input().strip()
        except EOFError:
            break
        print('Resistente' if s in d else 'Nao resistente')
main()
