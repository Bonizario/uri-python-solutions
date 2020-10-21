# STRINGS, UPPERCASE E LOWERCASE INTERCALADAS ([a-zA-Z] e ' ')
def main():
    from sys import stdout
    while True:
        try:
            sentence = input() # stdin.readline() causes a TLE error
        except Exception:
            break
        counter = 0
        dancing = ''
        for i in range(len(sentence)):
            c = sentence[i]
            if c == ' ':
                dancing += ' '
            elif not counter:
                dancing += c.upper()
                counter ^= 1
            else:
                dancing += c.lower()
                counter ^= 1
        stdout.write('%s\n' % dancing)
main()
