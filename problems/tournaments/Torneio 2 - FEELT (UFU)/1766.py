# 1766 - O Elfo das Trevas
# BALSAQUE
for i in range(1, int(input()) + 1):
    print("CENARIO {" + str(i) + "}")

    totalRenas, renas = map(int, input().split())

    names = dict()
    for _ in range(totalRenas):
        name, weight, age, height = input().split()
        weight = int(weight)
        age = int(age)
        height = float(height)

        if weight not in names.keys():
            names[weight] = dict()
            names[weight][age] = dict()
            names[weight][age][height] = []
        elif age not in names[weight].keys():
            names[weight][age] = dict()
            names[weight][age][height] = []
        elif height not in names[weight][age].keys():
            names[weight][age][height] = []

        names[weight][age][height].append(name)

    i = 1
    for weight in sorted(names)[::-1]:
        for age in sorted(names[weight]):
            for height in sorted(names[weight][age]):
                for name in sorted(names[weight][age][height]):
                    if not len(names[weight][age][height]):
                        continue

                    toremove = min(names[weight][age][height])
                    print(str(i) + " - " + toremove)
                    names[weight][age][height].remove(toremove)

                    i += 1
                    if i == renas + 1:
                        break
                if i == renas + 1:
                    break
            if i == renas + 1:
                break
        if i == renas + 1:
            break
