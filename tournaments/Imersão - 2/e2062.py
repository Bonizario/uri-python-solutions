def main():
    n = int(input())
    words = input().split()
    for i, word in enumerate(words):
        if len(word) == 3:
            if word[0] == 'O' and word[1] == 'B':
                words[i] = 'OBI'
            elif word[0] == 'U' and word[1] == 'R':
                words[i] = 'URI'
        if i < n - 1:
            print(words[i], end=' ')
        else:
            print(words[i])
main()
