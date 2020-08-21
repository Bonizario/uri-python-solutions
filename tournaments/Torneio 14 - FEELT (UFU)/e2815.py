def main():
    from sys import stdin, stdout
    s = stdin.readline().strip().split()
    for i, word in enumerate(s):
        if len(word) >= 4 and word[0:2] == word[2:4]:
            s[i] = word[2:]
    stdout.write(f'{" ".join(s)}\n')
main()
