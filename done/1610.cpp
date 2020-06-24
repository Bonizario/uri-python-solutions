// 1610 - Dudu Service Maker (DETECT CICLES IN DIRECTED GRAPH)
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> adj[10001];
int visited[10001];
bool loop;

void dfs(int S) {
    visited[S] = 0; // being visited
    for (int i = 0; i < (int)adj[S].size(); i++) {
        if (visited[adj[S][i]] == -1) // never visited
            dfs(adj[S][i]);
        else if (visited[adj[S][i]] == 0) {
            loop = true;
            return;
        }
    }
    visited[S] = 1; // fully visited
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T, N, M, A, B;

    cin >> T;
    while (T--) {
        loop = false;

        cin >> N >> M;
        for (int i = 1; i <= N; i++) {
            adj[i].clear();
            visited[i] = -1;
        }

        for (int i = 1; i <= M; i++) {
            cin >> A >> B;
            // avoid pushing repeated nodes
            vector<int>::iterator it = find(adj[A].begin(), adj[A].end(), B);
            if (it == adj[A].end())
                adj[A].push_back(B);
        }

        for (int i = 1; i <= N; i++) {
            if (loop) break;
            dfs(i);
        }

        cout << (loop ? "SIM\n" : "NAO\n");
    }

    return 0;
}
