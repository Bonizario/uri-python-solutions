#include <iostream>
#define MAXN 10005

using namespace std;

int pai[MAXN], peso[MAXN];

int find(int x) {
    if (pai[x] == x) return x;
    return pai[x] = find(pai[x]);
}

void join(int x, int y) {
    x = find(x);
    y = find(y);
    if (x == y) return;
    if (peso[x] > peso[y]) pai[y] = x;
    else {
        pai[x] = y;
        if (peso[x] == peso[y]) peso[y]++;
    }
}


int main() {
    int i, N, M, Q, X, Y;
    bool hasPrinted = false;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    while (cin >> N >> M >> Q) {
        if (hasPrinted) cout << "\n";
        hasPrinted = true;

        for (i = 0; i < N; i++) {
            pai[i] = i;
        }

        for (i = 0; i < M; i++) {
            cin >> X >> Y;
            join(X-1, Y-1);
        }

        for (i = 0; i < Q; i++) {
            cin >> X >> Y;
            if (find(X-1) == find(Y-1)) {
                cout << "S\n";
            } else {
                cout << "N\n";
            }
        }
    }

    return 0;
}
