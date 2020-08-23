def main():
    from sys import stdin, stdout
    POSITIVE_INFINITY = float('inf')

    def reconstruct_path(start, end, dp, nxt):
        path = []

        if dp[start][end] == POSITIVE_INFINITY:
            return path
        at = start
        while at != end:
            # print(f'at: {at}, end: {end}, nxt[{at}][{end}] = {nxt[at][end]}\n')
            if at == -1:
                return None
            path.append(at)
            at = nxt[at][end]

        # if start == end
        if not path:
            path.append(start)
        #print(f'from {places[start]} to {places[end]} path => {path} OKOK\n')
        if nxt[at][end] == -1:
            return None
        path.append(end)
        #print(f'from {places[start]} to {places[end]} path => {path}')

        return path

    for _ in range(int(stdin.readline())):
        p = int(stdin.readline())

        # list of places
        places = stdin.readline().strip().split()

        # map place -> index
        parser = dict(zip(places, list(range(p))))
        # print(*parser.items())

        # dp - floyd warshall
        dp = [list(map(int, stdin.readline().split())) for _ in range(p)]

        # path
        nxt = [[-1] * p for _ in range(p)]

        for i in range(p):
            for j in range(p):
                if dp[i][j] != -1:
                    dp[i][j] = dp[i][j]
                    nxt[i][j] = j
                else:
                    dp[i][j] = POSITIVE_INFINITY
                    nxt[i][j] = -1

        for k in range(p):
            for i in range(p):
                for j in range(p):
                    if dp[i][k] + dp[k][j] < dp[i][j]:
                        dp[i][j] = dp[i][k] + dp[k][j]
                        nxt[i][j] = nxt[i][k]

        for _ in range(int(stdin.readline())):
            name, place1, place2 = stdin.readline().strip().split()
            start, end = parser[place1], parser[place2]

            path = reconstruct_path(start, end, dp, nxt)
            if not path:
                stdout.write(f'Sorry Mr {name} you can not go from {place1} to {place2}\n')
            else:
                stdout.write(f'Mr {name} to go from {place1} to {place2}, you will receive {dp[start][end]} euros\n')
                stdout.write(f'Path:{" ".join(str(places[place_index]) for place_index in path)}\n')

main()
