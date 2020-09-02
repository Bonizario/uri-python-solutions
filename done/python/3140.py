def main():
    from sys import stdin, stdout

    body = False
    while True:
        try:

            line = stdin.readline()
            if not line:
                break
            if '</body>' in line:
                body = False
            if body:
                stdout.write(line)
            if '<body>' in line:
                body = True
        except:
            break

main()
