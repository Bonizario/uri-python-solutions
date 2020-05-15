# 1222 - CHARACTERS, LINES, PAGES, PAGINATION
def main():
    from sys import stdin, stdout

    while True:
        try:
            words, max_lines, max_chars = [int(x) for x in stdin.readline().rstrip().split()]
        except Exception:
            break

        words_lengths = tuple((map(lambda w: len(w), stdin.readline().rstrip().split())))

        lines = 0
        chars = 0
        for i in range(words):
            if i == 0: # first word doesn't have blank space
                length = words_lengths[i]
            else:
                length = words_lengths[i] + 1

            if chars+length <= max_chars:
                chars += length
            else:
                lines += 1 # add one page after reaching the character limit per page
                chars = length - 1 # first word of the next lines, last word of the text

        lines += 1 # add another page for the remaining characters

        if lines % max_lines == 0:
            pages = lines//max_lines
        else:
            pages = lines//max_lines + 1

        stdout.write('%d\n' % pages)

if __name__ == '__main__':
    main()
