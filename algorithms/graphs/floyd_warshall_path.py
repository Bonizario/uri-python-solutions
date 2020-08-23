def main():
    POSITIVE_INFINITY = float('inf')
    NEGATIVE_INFINITY = float('-inf')

    def propagate_negative_cycles(n, dp):
        '''
        Execute fw again and if the distance can be improved,
        there is a negative cycle.

        Set the distance to -inf.

        Every edge i -> j marked with -inf is either part of or
        reaches into a negative cycle.
        '''
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dp[i][k] + dp[k][j] < dp[i][j]:
                        dp[i][j] = NEGATIVE_INFINITY
                        nxt[i][j] = -1


    def reconstruct_path(n, dp, start, end):
        '''
        Return an empty list if the start and end nodes
        are not connected.

        Return None if the path from start to end is affected
        by a negative cycle.

        Return a non-empty list with node indexes representing
        the shortest path from the start node to the end node (inclusive).

        This function should only be called after running floyd_warshall.
        '''
        path = []

        # a path between the start and the end node must exist
        if dp[start][end] == POSITIVE_INFINITY:
            return path

        at = start
        while at != end:
            if at == -1:
                return None
            path.append(at)
            at = nxt[at][end]

        # if start == end, the path is still empty
        if not path:
            path.append(start)

        if nxt[at][end] == -1:
            return None

        path.append(end)
        return path


    def floyd_warshall(n, dp, nxt):
        '''
        In graph theory, Floyd Warshall (FW) algorithm
        is an All-Pairs Shortest Path (APSP) algorithm.

        It can find the shortest path between all pairs of nodes.

        FW is also good to detect negative cycles, and ideal
        for graphs no larger than a couple hundred of nodes.

        Time complexity: O(V^3)
        '''
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dp[i][k] + dp[k][j] < dp[i][j]:
                        dp[i][j] = dp[i][k] + dp[k][j]
                        nxt[i][j] = nxt[i][k]

        # detect and propagate negative cycles
        propagate_negative_cycles(n, dp)

        return dp
