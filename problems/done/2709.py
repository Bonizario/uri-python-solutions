# 2709 - The Coins of Robbie
import sys
sys.stdout = open(sys.stdout.buffer.fileno(), 'w', encoding='utf8')

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, x):  # 2 doesn't entry the loop
        if x % i == 0:
            return False
    return True

win = "You’re a coastal aircraft, Robbie, a large silver aircraft.\n"
lose = "Bad boy! I’ll hit you.\n"

while True:
    try:
        V = 0
        M = int(input())
        coins = [int(input()) for _ in range(M)]
        jump = int(input())
        for i in range(M - 1, -1, -jump):
            V += coins[i]
        if is_prime(V):
            sys.stdout.buffer.write(win.encode())
        else:
            sys.stdout.buffer.write(lose.encode())
    except EOFError:
        break
