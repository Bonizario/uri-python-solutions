# 2651 - Upset Link
def main():
    from sys import stdin, stdout
    s = stdin.readline().lower()
    if 'zelda' in s:
        stdout.write("Link Bolado\n")
    else:
        stdout.write("Link Tranquilo\n")
if __name__ == '__main__':
    main()
