#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100000;

vector<int> adj[MAXN]; // Adjacency List

int main() {
    int N, M; // Nodes, Edges
    cin >> N >> M;

    int A, B;
    for (int i = 1; i <= M; i++) {
        cin >> A >> B;
        adj[A].push_back(B);
        adj[B].push_back(A); // For undirected graphs
    }

    // Code [...]

    return 0;
}
