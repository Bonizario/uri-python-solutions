/*
    Kruskal's algorithm is a minimum-spanning-tree algorithm which finds an edge
    of the least possible weight that connects any two trees in the forest.
    It is a greedy algorithm in graph theory as it finds a minimum spanning tree
    for a connected weighted graph adding increasing cost arcs at each step.
    This means it finds a subset of the edges that forms a tree that includes
    every vertex, where the total weight of all the edges in the tree is
    >minimized<.
*/
#include <iostream>
#include <algorithm>
#define MAXN 100001 // max number of nodes
#define MAXM 100001 // max number of edges

using namespace std;

struct t_edge {
    int cost, x, y;
};

bool comp(t_edge a, t_edge b) {
    return a.cost < b.cost; // could be '>' to maximize the weights
}

t_edge edge[MAXM], mst[MAXM]; // input -> edge; mst -> output


int parent[MAXM], weight[MAXM]; // union find functions

int find(int x) {
    if (x == parent[x]) return x;
    return parent[x] = find(parent[x]);
}

void join(int x, int y) {
    x = find(x);
    y = find(y);

    if (x == y) return;

    if (parent[x] < parent[y]) parent[x] = y;
    else if (parent[y] < parent[x]) parent[y] = x;
    else {
        parent[y] = x;
        weight[x]++;
    }
}

int main() {
    ios_base::sync_with_stdio(false); // fast I/O
    cin.tie(NULL);

    int i, N, M;
    cin >> N >> M;

    for(i = 1; i <= M; i++) // reading input
        cin >> edge[i].x >> edge[i].y >> edge[i].cost;


    for (i = 1; i <= N; i++) { // union find setup
        parent[i] = i;
        weight[i] = 0;
    }

    sort(edge+1, edge+1+M, comp);

    int size = 0;
    for (i = 1; i <= M; i++) {
        if (find(edge[i].x) != find(edge[i].y)) { // diferent parents
            join(edge[i].x, edge[i].y);

            mst[++size] = edge[i];
        }
    }

    for (i = 1; i < N; i++) // printing the minimum-spanning-tree
        cout << mst[i].x << " " << mst[i].y << " " << mst[i].cost << "\n";


    return 0;
}
