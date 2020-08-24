def main():
    from sys import stdin, stdout
    MOD = 2147483647

    power = int(stdin.readline())
    base = 3
    result = 1
    while power > 0:
        if power & 1:  # if power is odd
            result = (result * base) % MOD
        power = power // 2  # divide the power by 2
        base = (base * base) % MOD  # multiply base to itself

    stdout.write('%d\n' % result)

main()
