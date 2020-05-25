# 1025 - BINARY SEARCH -> 1ST OCCURENCE OF A VALUE
def main():
    from sys import stdin, stdout

    def binary_search_1st_occurence(elements, value, N):
        left = 0
        right = N - 1
        ans = -1

        while left <= right:
            middle = left + (right - left) // 2

            if elements[middle] == value:
                ans = middle
            if elements[middle] >= value:
                right = middle - 1
            else:
                left = middle + 1
        return ans

    case = 1
    while True:
        N, Q = [int(x) for x in stdin.readline().split()]
        if N == 0 and Q == 0:
            break
        stdout.write('CASE# %d:\n' % case)
        marbles = [int(stdin.readline()) for _ in range(N)]
        marbles.sort()
        for _ in range(Q):
            query = int(stdin.readline())
            index = binary_search_1st_occurence(marbles, query, N)
            if index != -1:
                stdout.write('%d found at %d\n' % (query, index+1))
            else:
                stdout.write('%d not found\n' % query)
        case += 1


main()
