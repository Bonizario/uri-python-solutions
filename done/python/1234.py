# 1234 - STRINGS, UPPERCASE E LOWERCASE INTERCALADAS ([a-zA-Z] e ' ')
def main():
    from sys import stdout
    while True:
        try:
            sentence = input() # using stdin.readline() causes an tle error
        except Exception:
            break
        counter = 0
        dancing = ''
        for i in range(len(sentence)):
            c = sentence[i]
            if c == ' ':
                dancing += ' '
            elif counter == 0:
                dancing += c.upper()
                counter += 1
            elif counter > 0:
                dancing += c.lower()
                counter -= 1
        stdout.write('%s\n' % dancing)

if __name__ == '__main__':
    main()
