# 1582 - The Pythagorean Theorem
def mdc(x, y):
    while y != 0:
        x, y = y, x % y
    return x

while True:
    try:
        x, y, z = [int(x) for x in input().split()]
        if (x > y) and (x > z) and (x*x == y*y + z*z):
            if mdc(z, (mdc(x, y))) == 1:
                print('tripla pitagorica primitiva')
            else:
                print('tripla pitagorica')
        elif (y > x) and (y > z) and (y*y == x*x + z*z):
            if mdc(z, (mdc(x, y))) == 1:
                print('tripla pitagorica primitiva')
            else:
                print('tripla pitagorica')
        elif (z > x) and (z > y) and (z*z == x*x + y*y):
            if mdc(z, (mdc(x, y))) == 1:
                print('tripla pitagorica primitiva')
            else:
                print('tripla pitagorica')
        else:
            print('tripla')
    except:
        break
