# 1279 - Leap Year or Not Leap Year
def main():
    from sys import stdin, stdout
    year = stdin.readline().rstrip()
    while year:
        last4 = year[-4:]
        last2 = year[-2:]
        last2_int = int(last4)
        last = year[-1]
        total_sum = 0
        total_even = 0
        total_odd = 0
        leap = False
        huluculu = False
        bulukulu = False

        even = True
        for i in range(len(year)):
            digit = int(year[i])
            total_sum += digit
            if even:
                total_even += digit
            else:
                total_odd += digit
            even = not even

        if last2_int % 4 == 0 and last2 != '00':
            leap = True
        if int(last4[:2]) % 4 == 0 and last2 == '00':
            leap = True
        if (total_sum % 3 == 0) and (last == '0' or last == '5'):
            huluculu = True
        if (total_odd-total_even) % 11 == 0 and (last == '0' or last == '5') and leap:
            bulukulu = True

        if leap:
            stdout.write('This is leap year.\n')
        if huluculu:
            stdout.write('This is huluculu festival year.\n')
        if bulukulu:
            stdout.write('This is bulukulu festival year.\n')
        if not leap and not huluculu and not bulukulu:
            stdout.write('This is an ordinary year.\n')

        try:
            year = stdin.readline().rstrip()
            if year:
                stdout.write('\n')
        except EOFError:
            break

if __name__ == '__main__':
    main()
