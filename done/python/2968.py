def main():
    from math import ceil

    v, n = map(int, input().split())
    relation = v * n / 10
    signs = [ceil(relation * i) for i in range(1, 10)]
    print(' '.join(map(str, signs)))

main()
