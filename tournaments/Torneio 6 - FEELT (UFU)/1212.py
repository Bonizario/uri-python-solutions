while True:
    a, b = input().split()
    a, b = a[::-1], b[::-1]
    if a == '0' and b == '0':
        break

    sizea, sizeb = len(a), len(b)

    if sizea < sizeb:
        sizea, sizeb = sizeb, sizea
        a, b = b, a
    count = carry = 0

    for i in range(sizea):
        s = int(a[i])
        if i < sizeb:
            s += int(b[i])
        s += carry

        if s > 9:
            carry = s // 10
            count += 1
        else:
            carry = 0

    print( (str(count) if count else 'No') + ' carry operation' + ('s.' if count > 1 else '.') )
