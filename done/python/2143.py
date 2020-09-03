def main():
    from sys import stdin, stdout

    while True:
        t = int(stdin.readline())
        if not t:
            break

        nums = [int(stdin.readline()) for _ in range(t)]
        ans = '\n'.join(map(str, (2 * n - 1 if n & 1 else 2 * n - 2 for n in nums)))
        stdout.write(f'{ans}\n')

main()
