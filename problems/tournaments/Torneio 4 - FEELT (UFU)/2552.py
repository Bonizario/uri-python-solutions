# 2552 - CheeseBreadSweeper
while True:
    try:
        N, M = map(int, input().split())
    except EOFError:
        break

    board = []
    for _ in range(N):
        board.append(list(map(lambda x: '9' if x == '1' else '0', input().split())))

    for i in range(N):
        for j in range(M):
            if board[i][j] == '0':
                cheesebread =  1 if i != 0   and board[i-1][j] == '9' else 0
                cheesebread += 1 if i != N-1 and board[i+1][j] == '9' else 0
                cheesebread += 1 if j != 0   and board[i][j-1] == '9' else 0
                cheesebread += 1 if j != M-1 and board[i][j+1] == '9' else 0
                board[i][j] = str(cheesebread)
        print(''.join(board[i]))
