// Recursive
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100000;

int component[MAXN];
vector<int> adj[MAXN];

void dfs(int s) {
    for (int i = 0; i < (int) adj[s].size(); i++) {
        int v = adj[s][i];

        if (component[v] == -1) {
            component[v] = component[s];
            dfs(v);
        }
    }
}

// Iterative
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100000;

bool visited[MAXN];

void dfs(const vector<vector<int>> & adj, int node) {
    stack<int> stk;
    stk.push(node);
    visited[node] = true;

    while (!stk.empty()) {
        node = stk.top();
        stk.pop();

        for (int i = 0; i < (int) adj[node].size(); i++) {
            int v = adj[node][i];
            if(!visited[v]) {
                stk.push(v);
                visited[v] = true;
            }
        }
    }
}
