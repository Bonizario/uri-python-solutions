def main():
    import re
    patterns = {
        0: re.compile(r'a|k|u|G|Q+'),
        1: re.compile(r'b|l|v|I|S+'),
        2: re.compile(r'c|m|w|E|O|Y+'),
        3: re.compile(r'd|n|x|F|P|Z+'),
        4: re.compile(r'e|o|y|J|T+'),
        5: re.compile(r'f|p|z|D|N|X+'),
        6: re.compile(r'g|q|A|K|U+'),
        7: re.compile(r'h|r|C|M|W+'),
        8: re.compile(r'i|s|B|L|V+'),
        9: re.compile(r'j|t|H|R+')
    }
    for _ in range(int(input())):
        text = input().strip().replace(' ', '')
        for i in range(10):
            text = re.sub(patterns[i], str(i), text)
        if len(text) > 12:
            text = text[:12]
        print(text)
main()
