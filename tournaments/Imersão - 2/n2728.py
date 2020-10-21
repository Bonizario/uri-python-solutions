def main():
    cobol = ['c', 'o', 'b', 'o', 'l']
    while True:
        try:
            text = input().strip().lower().split('-')
        except EOFError:
            break
        index = 0
        ok = False
        for word in text:
            if word[0] == cobol[index] or word[-1] == cobol[index]:
                index += 1
            if index == 5:
                ok = True
                break
        print('GRACE HOPPER' if ok else 'BUG')
main()
