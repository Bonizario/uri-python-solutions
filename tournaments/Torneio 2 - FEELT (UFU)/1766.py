# 1766 - O Elfo das Trevas
# BALSAQUE
def main():
    from sys import stdin, stdout

    for i in range(1, int(stdin.readline()) + 1):
        stdout.write('CENARIO {' + str(i) + '}\n')
        totalRenas, renas = [int(r) for r in stdin.readline().split()]
        names = dict()

        for _ in range(totalRenas):
            name, weight, age, height = stdin.readline().rstrip().split()
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
                        stdout.write(str(i) + ' - ' + toremove + '\n')
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

if __name__ == '__main__':
    main()
