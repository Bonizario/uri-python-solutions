def main():
    from sys import stdin, stdout

    def binary_search_1st_occurence(arr, target, n):
        bl, br, ans = 0, n - 1, -1

        while bl <= br:
            bm = bl + (br - bl) // 2
            if arr[bm] == target:
                ans = bm
            if arr[bm] >= target:
                br = bm - 1
            else:
                bl = bm + 1
        return ans

    case = 1
    while True:
        n, q = map(int, stdin.readline().split())
        if n == 0 and q == 0:
            break

        stdout.write(f'CASE# {case}:\n')
        marbles = [int(stdin.readline()) for _ in range(n)]
        marbles.sort()
        for _ in range(q):
            query = int(stdin.readline())
            index = binary_search_1st_occurence(marbles, query, n)
            if index != -1:
                stdout.write(f'{query} found at {index + 1}\n')
            else:
                stdout.write(f'{query} not found\n')
        case += 1

main()
