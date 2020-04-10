# 1165 - Prime Number
def is_prime(x):
    # if 1 was a possible input
    # if (n <= 1):
    #     return False
    for i in range(2, x):  # 2 doesn't entry the loop
        if (x % i == 0):
            return False
    return True


n = int(input())
for _ in range(n):
    x = int(input())
    if is_prime(x):
        print('{} eh primo'.format(x))
    else:
        print('{} nao eh primo'.format(x))
