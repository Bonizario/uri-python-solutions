def main():
    from sys import stdin, stdout
    from datetime import date

    while True:
        try:
            month, day = map(int, stdin.readline().split())
        except Exception:
            break

        if month == 12:
            if day > 25:
                stdout.write('Ja passou!\n')
            elif day == 25:
                stdout.write('E natal!\n')
            elif day == 24:
                stdout.write('E vespera de natal!\n')
            else:
                stdout.write(f'Faltam {25 - day} dias para o natal!\n')
        else:
            days = abs(date(2016, month, day) - date(2016, 12, 25)).days
            stdout.write(f'Faltam {days} dias para o natal!\n')

main()
