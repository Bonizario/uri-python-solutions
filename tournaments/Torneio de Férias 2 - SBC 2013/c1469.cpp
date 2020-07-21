#include <iostream>
#include <algorithm>
#define MAXN 501

using namespace std;

int n, m, q, pos[MAXN], idade[MAXN];
int antecessor[MAXN][MAXN];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    while (cin >> n >> m >> q) {
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                antecessor[i][j] = 0;

        for (int i = 1; i <= n; i++) {
            cin >> idade[i];
            pos[i] = i;
        }

        int x, y;
        for (int i = 1; i <= m; i++) {
            cin >> x >> y;
            antecessor[x][y] = 1;
        }

        // Floyd-Warshall
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                // se i eh antecessor de k, i sera antecessor de j somente se k eh antecessor de j
                if (antecessor[i][k]) {
                    for (int j = 1; j <= n; j++) {
                        antecessor[i][j] |= antecessor[k][j];
                    }
                }
            }
        }

        char op;
        for (int i = 1; i <= q; i++) {
            cin >> op;
            if (op == 'T') {
                cin >> x >> y;
                swap(pos[x], pos[y]);
                swap(idade[pos[x]], idade[pos[y]]);
            } else {
                cin >> x;
                x = pos[x];
                int maisJovem = 999;
                for (int i = 1; i <= n; i++) {
                    if (antecessor[i][x]) {
                        maisJovem = min(maisJovem, idade[i]);
                    }
                }

                if (maisJovem == 999)
                    cout << "*\n";
                else
                    cout << maisJovem << "\n";
            }
        }
    }

    return 0;
}
