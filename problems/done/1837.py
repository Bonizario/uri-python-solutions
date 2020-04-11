# 1837 - Preface
a, b = map(int, input().split())
if (a > 0 and b > 0):
    q = a // b
    r = a % b
    print(q, r)
elif a > 0 and b < 0:
    q = -(a // abs(b))
    r = a - b * q
    print(q, r)
elif a < 0 and b > 0:
    q = a // b
    r = a - b * q
    print(q, r)
else:
    b = abs(b)
    q = a // b
    r = a - b * q
    print(abs(q), abs(r))
# a = b * q + r
