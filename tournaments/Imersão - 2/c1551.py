def main():
    from collections import defaultdict
    for _ in range(int(input())):
        d = defaultdict(int)
        phrase = input().strip()
        for character in phrase:
            if 'a' <= character <= 'z':
                d[character] += 1
        size = len(d)
        if size == 26:
            print('frase completa')
        elif size >= 13:
            print('frase quase completa')
        else:
            print('frase mal elaborada')
main()
