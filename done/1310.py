# 1310 - Lucro
def main():
    from sys import stdin, stdout

    def kadane(n, arr):
        max_sum = curr_sum = 0
        for i in range(n):
            curr_sum = max(arr[i], curr_sum + arr[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum

    while True:
        try:
            n = int(stdin.readline())
        except:
            break
        cost = int(stdin.readline())
        revenues = [(int(stdin.readline()) - cost) for _ in range(n)]
        stdout.write(str(kadane(n, revenues)) + '\n')

main()
