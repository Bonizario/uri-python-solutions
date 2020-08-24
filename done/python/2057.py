# 2057 - Fuso Horário
def main():
    a, b, c = map(int, input().split())
    ans = a + b + c
    if ans < 0:
        print(24 + ans)
    elif ans > 24:
        print(ans - 24)
    else:
        print(ans)

main()
