# 1158 - Sum of Consecutive Odd Numbers III
def main():
    from sys import stdin, stdout

    for _ in range(int(stdin.readline())):
        X, Y = [int(x) for x in stdin.readline().split()]
        if X % 2 == 0:  # increment if X is even
            X += 1  # X must be odd before going to the loop
        if X % 2 != 0:
            result = X  # result starting value is X (odd number)
            for _ in range(Y - 1):  # Y - 1 to avoid exceeding the limit
                X += 2
                result += X
        print(result)

if __name__ == '__main__':
    main()
