# 2653 - Dijkstra
def main():
    from sys import stdout

    jewels = set()
    while True:
        try:
            jewels.add(input())
        except EOFError:
            break

    stdout.write(str(len(jewels)) + '\n')

if __name__ == '__main__':
    main()
