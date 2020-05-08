# 1520 - Screws and Nuts
while True:
    try:
        N = input().strip()
        N = int(N)
    except EOFError:
        break
    except:
        continue
    box = [0]*100
    for _ in range(N):
        entry = input().strip().split()
        start = int(entry[0])
        end = int(entry[1])
        for i in range(start-1, end):
            box[i] += 1
    screw = input().strip()
    screw = int(screw)
    if box[screw-1] == 0:
        print('{} not found'.format(screw))
    else:
        pos1 = 0
        for i in range(screw-1):
            pos1 += box[i]
        pos2 = pos1 + box[screw-1] - 1
        print('{} found from {} to {}'.format(screw, pos1, pos2))
