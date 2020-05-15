# 1243 - REGEX -> ONLY WORDS, OR WORDS *ENDING* WITH *ZERO* OR *ONE* DOT ('.')
def main():
    from sys import stdout
    from re import fullmatch

    while True:
        try:
            text = input().split()
        except EOFError:
            break

        # ^ matches start of string
        # [a-zA-Z]+ matches any letters, 1 or more times
        # \.? matches 0 OR 1 dot
        # $ matches end of string

        words = []
        for simbol in text:
            word = fullmatch(r'^[a-zA-Z]+\.?$', simbol) # returns None if the simbol isn't a word
            if word:
                words.append(word.group(0)) # .group(0) to convert match object into str

        if words:
            lengths = tuple((map(lambda w: len(w.rstrip('.')), words)))
            mean_length = sum(lengths)//len(lengths)
            if mean_length <= 3:
                stdout.write('250\n')
            elif mean_length == 4 or mean_length == 5:
                stdout.write('500\n')
            elif mean_length >= 6:
                stdout.write('1000\n')
        else:
            stdout.write('250\n')

if __name__ == '__main__':
    main()
