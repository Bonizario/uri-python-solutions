# 1237 - SIZE OF THE LARGEST COMMON SUBSTRING BETWEEN 2 STRINGS
def main():
    from sys import stdin, stdout
    while True:
        try:
            string1 = input()
            string2 = input()
        except EOFError:
            break

        lengths = [0]*50
        size1 = len(string1)
        size2 = len(string2)
        start = 0
        end = 0
        index = 49
        substring = False
        if size1 >= size2:
            for i in range(size1):
                end += 1
                if string1[start:end] in string2 and not substring:
                    substring = True
                elif string1[start:end] not in string2 and substring:
                    lengths[index] += end-start-1
                    substring = False
                    index -= 1
                if string1[start:end] in string2 and substring and end == size1:
                    lengths[index] += end-start # handling two equal strings
                if string1[start:end] not in string2:
                    start += 1
        else:
            for i in range(size2):
                end += 1
                if string2[start:end] in string1 and not substring:
                    substring = True
                elif string2[start:end] not in string1 and substring:
                    lengths[index] += end-start-1
                    substring = False
                    index -= 1
                if string2[start:end] in string1 and substring and end == size2:
                    lengths[index] += end-start # handling two equal strings
                if string2[start:end] not in string1:
                    start += 1

        lengths.sort() # same results as using if/else+largest value
        stdout.write('%d\n' % lengths[-1])
if __name__ == '__main__':
    main()
