def main():
    from sys import stdin, stdout

    tea = int(stdin.readline())
    correct = 0
    for guess in list(map(int, stdin.readline().split())):
        if guess == tea:
            correct += 1
    stdout.write('%d\n' % correct)
main()
