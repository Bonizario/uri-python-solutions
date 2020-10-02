def main():
    from sys import stdin, stdout

    toys = {'F': 0, 'M': 0}
    for _ in range(int(stdin.readline())):
        gender = stdin.readline().split()[1]
        toys[gender] += 1
    stdout.write('%d carrinhos\n' % toys['M'])
    stdout.write('%d bonecas\n' % toys['F'])
main()
