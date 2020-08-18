#include <bits/stdc++.h>
using namespace std;

const int MAXN = 500;
const int INF = 1e9;

int n, dp[MAXN][MAXN];

void floydWarshall(void) {
    // dp[u][v] is the weight from u -> v
    // If there isn't an edge, it will be INF
    // For u == v, dp[u][v] = 0

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
            }
        }
    }
}

void floydWarshallAncestor(void) {
    // If 'i' is an ancestor of 'k', 'i' will be an ancestor
    // of 'j' only if 'k' is an ancestor of 'j'

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            if (dp[i][k]) {
                for (int j = 0; j < n; j++) {
                    dp[i][j] |= dp[k][j];
                }
            }
        }
    }
}
