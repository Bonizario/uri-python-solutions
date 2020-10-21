def main():
    n = int(input())
    s = set(range(1, n + 1))
    for num in map(int, input().split()):
        s.discard(num)
    print(*s)
main()
