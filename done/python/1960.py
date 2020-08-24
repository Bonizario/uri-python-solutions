def main():
    from sys import stdin, stdout

    i = 12
    nums = [1,4,5,9,10,40,50,90,100,400,500,900,1000];
    parser = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    n = int(stdin.readline())

    while n > 0:
        div = n // nums[i]
        n %= nums[i]
        while div:
            div -= 1
            stdout.write(parser[i])
        i -= 1
    stdout.write('\n')

main()
