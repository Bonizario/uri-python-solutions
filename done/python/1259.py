def main():
    from sys import stdin, stdout

    n = int(stdin.readline())
    nums = [int(stdin.readline()) for _ in range(n)]
    even, odd = [], []
    for num in nums:
        if num & 1:
            odd.append(num)
        else:
            even.append(num)
    even.sort()
    odd.sort(reverse=True)
    even.extend(odd)
    stdout.write('\n'.join(map(str, even)) + '\n')
main()
