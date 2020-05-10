# 2715 - Dividindo os Trabalhos I
# BALSAQUE
def main():
    from sys import stdin, stdout
    while True:
        try:
            n = int(stdin.readline())
            numbers = [int(x) for x in stdin.readline().split()]

            total = sum(numbers)
            sum_numbers = 0
            difference = total

            for i in range(len(numbers)):
                sum_numbers += numbers[i]
                new_diff = abs(total - sum_numbers * 2)

                if new_diff < difference:
                    difference = new_diff
                else:
                    break
                if not difference:
                    break
            stdout.write(str(difference) + '\n')
        except Exception:
                break

if __name__ == '__main__':
    main()
