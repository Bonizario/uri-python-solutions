def main():
    import re
    pattern = re.compile(r'([0-9]+)+')
    for _ in range(int(input())):
        text = input().strip()
        print(sum(map(int, re.findall(pattern, text))))
main()
