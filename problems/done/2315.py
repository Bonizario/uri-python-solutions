# 2315 - Easy Difference Between Dates
def main():
    from sys import stdin, stdout
    from datetime import date

    day1, month1 = [int(x) for x in stdin.readline().split()]
    day2, month2 = [int(x) for x in stdin.readline().split()]
    first_date = date(2021, month1, day1)
    last_date = date(2021, month2, day2)
    days = (last_date-first_date).days

    stdout.write(str(days) + '\n')

if __name__ == '__main__':
    main()
