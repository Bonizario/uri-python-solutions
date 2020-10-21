def main():
    from sys import stdin, stdout
    line = int(stdin.readline())
    operation = stdin.readline().strip()
    matrix = [[float(stdin.readline()) for _ in range(12)] for _ in range(12)]
    result = sum(matrix[line])
    stdout.write('{:.1f}\n'.format(result if operation == 'S' else result / 12.0))
main()
