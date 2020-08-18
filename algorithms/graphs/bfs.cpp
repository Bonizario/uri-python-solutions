#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100000;

bool visited[MAXN];

void bfs(const vector<vector<int>> &adj, int node) {
    queue<int> Lst;
    Lst.push(node);
    visited[node] = true;

    while (!Lst.empty()) {
        node = Lst.front();
        Lst.pop();

        for (int i = 0; i < (int) adj[node].size(); i++) {
            int v = adj[node][i];
            if (!visited[v]) {
                visited[v] = true;
                Lst.push(v);
            }
        }
    }
}
