def main():
    from sys import stdin, stdout
    for i in range(int(stdin.readline())):
        stdout.write('\n' if i else '')
        m, c = map(int, stdin.readline().split())
        nums = list(map(int, stdin.readline().split()))
        hash_table = [[] for _ in range(m)]
        for num in nums:
            hash_table[num % m].append(num)
        for i, line in enumerate(hash_table):
            stdout.write('{}{}'.format(i, ' -> ' if line else ''))
            stdout.write(' -> '.join(map(str, line)) + ' -> \\\n')
main()
