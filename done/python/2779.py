def main():
    from sys import stdin, stdout

    total = int(stdin.readline())
    bought = set()
    for _ in range(int(stdin.readline())):
        bought.add(int(stdin.readline()))
    stdout.write(f'{total - len(bought)}\n')

main()
