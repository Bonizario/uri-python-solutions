# 1244 - Sort by Length
def main():
    for _ in range(int(input())):
        print(' '.join(text for text in sorted(input().split(), key=len, reverse=True)))
main()
