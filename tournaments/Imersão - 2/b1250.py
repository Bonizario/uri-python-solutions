def main():
    for _ in range(int(input())):
        ans = 0
        t = int(input())
        heights = list(map(int, input().split()))
        actions = list(input().strip())
        for height, action in zip(heights, actions):
            if (action == 'S' and height <= 2) or (action == 'J' and height > 2):
                ans += 1
        print(ans)
main()
