def main():
    for _ in range(int(input())):
        n = int(input())
        odd_numbers = sorted(x for x in map(int, input().split()) if x & 1)
        ans = []
        a, b = 0, -1
        if not odd_numbers:
            print()
            continue
        for i in range(len(odd_numbers)):
            if i & 1:
                ans.append(odd_numbers[a])
                a += 1
            else:
                ans.append(odd_numbers[b])
                b -= 1
        print(' '.join(map(str, ans)))
main()
