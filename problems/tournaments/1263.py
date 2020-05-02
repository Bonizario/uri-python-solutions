# 1263 - Alliteration
while True:
    try:
        words = input().lower().split()
        allits = 0
        last = ''
        alliting = False
        for word in words:
            if word[0] == last:
                if not alliting:
                    allits += 1
                    alliting = True
            else:
                alliting = False
            last = word[0]
        print(allits)
    except EOFError:
        break
