# 2715 - Dividindo os Trabalhos I
# BALSAQUE
while True:
    try:
        n = int(input())
        numbers = list(map(int, input().split()))

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
        print(difference)
    except EOFError:
            break
