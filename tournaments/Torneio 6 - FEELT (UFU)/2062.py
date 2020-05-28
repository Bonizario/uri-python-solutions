N = int(input())
text = input().split()
for i in range(len(text)):
    word = text[i]
    if len(word) == 3:
        if word[:2] == 'OB' or word[:2] == 'UR':
            text[i] = word[:2] + 'I'

print(' '.join(text))
