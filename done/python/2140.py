def main():
    from sys import stdin, stdout

    while True:
        n, m = map(int, stdin.readline().split())
        if n == m == 0:
            break

        bills, change = [], m - n

        bills.append(change // 100)
        change %= 100

        bills.append(change // 50)
        change %= 50

        bills.append(change // 20)
        change %= 20

        bills.append(change // 10)
        change %= 10

        bills.append(change // 5)
        change %= 5

        bills.append(change // 2)

        valid = sum(bills) == 2

        stdout.write('possible\n' if valid else 'impossible\n')

main()
