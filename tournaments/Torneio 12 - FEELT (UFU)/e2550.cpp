#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n, m, G[1001], S[1001];

struct Predio {
    int A, B, C;
};

bool cmp(Predio X, Predio Y) {
    return X.C < Y.C;
}

int Find(int A) {
    if (G[A] == A) return A;
    return G[A] = Find(G[A]);
}

void Union(int A, int B) {
    A = Find(A), B = Find(B);

    if (A == B)
        return;
    if (S[A] < S[B]) {
        G[A] = B;
        S[B] += S[A];
    } else {
        G[B] = A;
        S[A] += S[B];
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<Predio> vias, mst;
    vias.resize(499501), mst.resize(499501);

    while (cin >> n >> m) {
        for (int i = 1; i <= n; i++)
            G[i] = i, S[i] = 1;

        vias.clear(), mst.clear();
        for (int i = 1; i <= m; i++)
            cin >> vias[i].A >> vias[i].B >> vias[i].C;

        sort(vias.begin() + 1, vias.begin() + 1 + m, cmp);

        unsigned tamanho = 0;
        for (int i = 1; i <= m; i++) {
            if (Find(vias[i].A) != Find(vias[i].B)) {
                Union(vias[i].A, vias[i].B);
                mst[++tamanho] = vias[i];
            }
        }

        unsigned status = 0;
        for (int i = 1; i <= n; i++) {
            if (G[i] == i)
                status++;
            if (status > 1) {
                cout << "impossivel\n";
                break;
            }
        }

        if (status == 1) {
            unsigned ans = 0;
            for (int i = 1; i < n; i++)
                ans += mst[i].C;
            cout << ans << "\n";
        }
    }

    return 0;
}
