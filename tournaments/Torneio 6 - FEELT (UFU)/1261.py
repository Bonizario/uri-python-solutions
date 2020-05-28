mydict = dict()
M, N = [int(x) for x in input().split()]
for _ in range(M):
    word, value = input().split()
    mydict[word] = int(value)

while True:
    try:
        total = 0
        while True:
            text = input()
            if text == '.':
                print(total)
                break
            text = text.split()

            for word in text:
                if word in mydict.keys():
                    total += mydict[word]

    except EOFError:
        break
