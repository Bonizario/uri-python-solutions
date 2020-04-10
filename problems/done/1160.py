# 1160 - Population Increase
t = int(input())
for _ in range(t):
    pa, pb, g1, g2 = map(float, input().split())
    time = 0
    while pa <= pb:
        pa += int(pa * g1 / 100)
        pb += int(pb * g2 / 100)
        time += 1
        if time > 100:
            print('Mais de 1 seculo.')
            break
    if time <= 100:
        print('{} anos.'.format(time))
