def main():
    for _ in range(int(input())):
        d = {}
        for _ in range(int(input())):
            item, action = input().split()
            if item not in d and action == 'chirrin':
                d[item] = 1
            elif item in d and action == 'chirrion':
                d.pop(item)
        print('TOTAL')
        for item in sorted(d.keys()):
            print(item)
main()
