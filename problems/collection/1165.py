# 1165 - PRIME NUMBER
def main():
    from sys import stdin, stdout

    for _ in range(int(stdin.readline())):
        X = int(stdin.readline())

        if X == 1:
            stdout.write('1 nao eh primo\n')
            continue

        prime = 1
        i = 2
        while i*i <= X:
            if X % i == 0: # check if i divides X without leaving a remainder
                prime = 0
                break
            i += 1

        if prime:
            stdout.write('%d eh primo\n' % X)
        else:
            stdout.write('%d nao eh primo\n' % X)

if __name__ == '__main__':
    main()

# def is_prime(n): # n >= 1
#     if n == 1:
#         return False

#     i = 2
#     while i*i <= n: # loop from 2 to int(sqrt(x))
#         if n % i == 0: # check if i divides x without leaving a remainder
#             return False # so it is not a prime number
#         i += 1
#     return True
