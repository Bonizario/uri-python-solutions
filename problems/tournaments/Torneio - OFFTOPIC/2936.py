# 2936 - How Much Cassava?
def main():
    from sys import stdin, stdout

    cu = int(stdin.readline()) * 300
    ba = int(stdin.readline()) * 1500
    bo = int(stdin.readline()) * 600
    ma = int(stdin.readline()) * 1000
    ia = int(stdin.readline()) * 150
    g = cu + ba + bo + ma + ia + 225

    stdout.write('%d\n' % g)

if __name__ == '__main__':
    main()
