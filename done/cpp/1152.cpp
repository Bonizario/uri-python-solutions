#include <iostream>
#include <algorithm>

using namespace std;

const unsigned MxN = 2e5;

struct Node {
    unsigned x, y, z;
};

bool comp(Node a, Node b) {
    return a.z < b.z;
}

unsigned G[MxN], S[MxN];

unsigned Find(unsigned a) {
    if (G[a] == a) return a;
    return G[a] = Find(G[a]);
}

unsigned Union(unsigned a, unsigned b) {
    a = Find(a);
    b = Find(b);
    if (a == b) return -1;
    if (S[a] < S[b]) {
        G[a] = b;
        S[b] += S[a];
        return b;
    } else {
        G[b] = a;
        S[a] += S[b];
        return a;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    unsigned i, n, m, prev_cost, cost, g;
    while (true) {
        cin >> n >> m; // Nodes, Edges
        if (n == 0 && m == 0) break;
        for (i = 0; i < n; i++) {
            G[i] = i;
            S[i] = 1;
        }

        Node C[m];
        prev_cost = 0;
        for (i = 0; i < m; i++) {
            cin >> C[i].x >> C[i].y >> C[i].z;
            prev_cost += C[i].z;
        }

        sort(C, C+m, comp);

        cost = 0;
        for (i = 0; i < m; i++) {
            //cout << "i=" << i << " x=" << C[i].x << " y=" << C[i].y<<"\n";
            g = Union(C[i].x, C[i].y);
            //cout << "g eh: " << g << "\n";
            if (g != -1) {
                //cout << C[i].x << " " << C[i].y << " " << g << "\n";
                cost += C[i].z;
                if (S[g] == n) break;
            }
        }
        //cout << prev_cost << " " << cost << "\n";
        //cout << "tamanho: " << S[g] << "\n";
        cout << prev_cost - cost << "\n";
    }

    return 0;
}
