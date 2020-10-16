def main():
    from sys import stdin, stdout

    def check_ladder_format(n, m, matrix):
        last_index = -1
        all_zeros = False
        for i in range(n):
            curr_index = -1
            for j, num in enumerate(matrix[i]):
                if num != 0:
                    if all_zeros:
                        return False
                    curr_index = j
                    break
            if curr_index == -1:
                all_zeros = True
            else:
                if curr_index <= last_index:
                    return False
                last_index = curr_index
        return True

    n, m = map(int, stdin.readline().split())
    matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
    stdout.write('S\n' if check_ladder_format(n, m, matrix) else 'N\n')

main()
