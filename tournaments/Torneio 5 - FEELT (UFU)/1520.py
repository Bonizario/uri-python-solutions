# 1520 - Screws and Nuts
def main():
    while True:
        try:
            N = int(input())
        except EOFError:
            break
        except:
            continue

        screws = [0]*100
        for _ in range(N):
            start, end = map(int, input().split())
            for i in range(start-1, end):
                screws[i] += 1

        screw = int(input())
        if screws[screw-1] == 0:
            print('{} not found'.format(screw))
        else:
            pos1 = 0
            for i in range(screw-1):
                pos1 += screws[i]
            pos2 = pos1 + screws[screw-1] - 1
            print('{} found from {} to {}'.format(screw, pos1, pos2))

if __name__ == '__main__':
    main()
