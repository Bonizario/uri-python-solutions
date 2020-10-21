def main():
    from sys import stdin, stdout

    case = 4
    for _ in range(int(stdin.readline())):
        if case > 4:
            stdout.write('\n')
        m = int(stdin.readline())
        digits = [0] * m
        matrix = [list(map(int, stdin.readline().split())) for _ in range(m)]

        for i in range(m):
            for j in range(m):
                matrix[i][j] *= matrix[i][j]
                if digits[j] < matrix[i][j]:
                    digits[j] = matrix[i][j]

        digits = list(map(lambda x: len(str(x)), digits))
        stdout.write('Quadrado da matriz #{}:\n'.format(case))
        case += 1
        for i in range(m):
            for j in range(m):
                if j == 0:
                    stdout.write('{num:{width}}'.format(num=matrix[i][j], width=digits[j]))
                else:
                    stdout.write(' {num:{width}}'.format(num=matrix[i][j], width=digits[j]))
            stdout.write('\n')
main()
