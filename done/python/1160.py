# 1160 - Population Increase
def main():
    from sys import stdin, stdout

    for _ in range(int(stdin.readline())):
        pa, pb, g1, g2 = [float(x) for x in stdin.readline().split()]
        time = 0
        while pa <= pb:
            pa += int(pa * g1 / 100)
            pb += int(pb * g2 / 100)
            time += 1
            if time > 100:
                stdout.write('Mais de 1 seculo.\n')
                break
        if time <= 100:
            stdout.write('%d anos.\n' % time)

if __name__ == '__main__':
    main()
