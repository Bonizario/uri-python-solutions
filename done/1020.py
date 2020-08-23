# 1020 - Age in Days
def main():
    from sys import stdin, stdout

    days = int(stdin.readline())
    years = days // 365
    years_rest = days % 365
    months = years_rest // 30
    months_rest = years_rest % 30

    stdout.write('%d ano(s)\n' % years)
    stdout.write('%d mes(es)\n' % months)
    stdout.write('%d dia(s)\n' % months_rest)

if __name__ == '__main__':
    main()
