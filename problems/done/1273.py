# 1273 - Justifier
def main():
    first = True
    while True:
        N = input()
        if N == '0':
            break
        if first:
            first = False
        else:
            print()
        N = int(N)
        largest = 0
        texts = []
        for _ in range(N):
            text = input()
            texts.append(text)
            if len(text) > largest:
                largest = len(text)
        print('\n'.join(['{:>{width}}'.format(text, width=largest) for text in texts]))
if __name__ == '__main__':
    main()
