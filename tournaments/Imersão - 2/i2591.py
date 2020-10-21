def main():
    for _ in range(int(input())):
        attack = input().split('k')
        print('k' + 'a' * (attack[0].count('a') * attack[1].count('a')))
main()
