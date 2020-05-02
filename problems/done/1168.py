# 1168 - LED
for _ in range(int(input())):
    leds = 0
    n = input()

    leds += 2 * n.count('1')
    leds += 4 * n.count('4')
    leds += 3 * n.count('7')
    leds += 5 * (n.count('2') + n.count('3') + n.count('5'))
    leds += 6 * (n.count('6') + n.count('9') + n.count('0'))
    leds += 7 * n.count('8')

    print('{} leds'.format(leds))
