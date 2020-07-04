#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

typedef pair<int, int> pii;

int n, m, G[1001], S[1001];

struct Computador {
    int A, B;
    double dist;
};

bool cmp(Computador X, Computador Y) {
    return X.dist < Y.dist;
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

double calcDist(pii A, pii B) {
    double x = B.first - A.first;
    double y = B.second - A.second;
    return sqrt(x * x + y * y);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    vector<Computador> cabos, mst;
    vector<pii> c;
    cabos.resize(124751), mst.resize(124751), c.resize(501);

    while (cin >> n) {
        for (int i = 1; i <= n; i++)
            G[i] = i, S[i] = 1;

        unsigned tamanho = n * (n - 1) / 2;
        cabos.clear(), mst.clear(), c.clear();

        for (int i = 1; i <= n; i++)
            cin >> c[i].first >> c[i].second;

        unsigned cont = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                cabos[cont].A = i, cabos[cont].B = j;
                cabos[cont].dist = calcDist(c[i], c[j]);
                cont++;
            }
        }

        sort(cabos.begin() + 1, cabos.begin() + 1 + tamanho, cmp);

        cont = 0;
        for (int i = 1; i <= tamanho; i++) {
            if (Find(cabos[i].A) != Find(cabos[i].B)) {
                Union(cabos[i].A, cabos[i].B);
                mst[++cont] = cabos[i];
            }
        }

        double ans = 0;
        for (int i = 1; i < n; i++)
            ans += mst[i].dist;

        cout.precision(2);
        cout.setf(ios::fixed);
        cout << ans << "\n";
    }

    return 0;
}
