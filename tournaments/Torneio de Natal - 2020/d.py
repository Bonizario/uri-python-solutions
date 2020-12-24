def main():
    n = int(input())
    conversor = dict()
    good_deeds = list(map(int, input().split()))
    for i, deed in enumerate(sorted(set(good_deeds))):
        conversor[deed] = i + 1
    print(sum(conversor[deed] for deed in good_deeds))
main()
