# 1239 - REPLACE '__', '**' -> '<i></i>', '<b></b>'
def main():
    from sys import stdout
    while True:
        try:
            text = input()
        except EOFError:
            break

        i = 0
        italic = False
        bold = False
        while True:
            try:
                if text[i] == '_' and not italic:
                    text = text[:i] + '<i>' + text[i+1:]
                    italic = True
                    i += 2
                elif text[i] == '_' and italic:
                    text = text[:i] + '</i>' + text[i+1:]
                    italic = False
                    i += 3
                elif text[i] == '*' and not bold:
                    text = text[:i] + '<b>' + text[i+1:]
                    bold = True
                    i += 2
                elif text[i] == '*' and bold:
                    text = text[:i] + '</b>' + text[i+1:]
                    bold = False
                    i += 3
                i += 1
            except Exception:
                stdout.write('%s\n' % text)
                break

if __name__ == '__main__':
    main()
