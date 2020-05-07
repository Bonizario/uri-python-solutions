# 1451 - Broken Keyboard
while True:
    try:
        entry = input()
    except EOFError:
        break

    pos1 = 0
    home = False
    processed = ''
    for pos2 in range(len(entry)):
        if entry[pos2] == '[' or entry[pos2] == ']':
            if home:
                processed = entry[pos1:pos2] + processed
            else:
                processed = processed + entry[pos1:pos2]
            home = entry[pos2] == '['
            pos1 = pos2 + 1
    if home:
        processed = entry[pos1:] + processed
    else:
        processed = processed + entry[pos1:]

    print(processed)
