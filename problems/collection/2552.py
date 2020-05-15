# 2552 - CAMPO MINADO / MINESWEEPER
def main():
    from sys import stdin, stdout

    while True:
        try:
            N, M = [int(x) for x in stdin.readline().split()]
        except Exception:
            break

        board = []
        for _ in range(N):
            board.append(list(map(lambda x: '9' if x == '1' else '0', stdin.readline().split())))
        for i in range(N):
            for j in range(M):
                if board[i][j] == '0':
                    cheesebread =  1 if i != 0   and board[i-1][j] == '9' else 0
                    cheesebread += 1 if i != N-1 and board[i+1][j] == '9' else 0
                    cheesebread += 1 if j != 0   and board[i][j-1] == '9' else 0
                    cheesebread += 1 if j != M-1 and board[i][j+1] == '9' else 0
                    board[i][j] = str(cheesebread)
            stdout.write(''.join(board[i]) + '\n')

if __name__ == '__main__':
    main()
