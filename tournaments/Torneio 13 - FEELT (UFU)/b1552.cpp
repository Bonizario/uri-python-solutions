// T13 => 1500, 1552, 1804, 2519, 2531, 2722
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

typedef pair<int, int> pii;

int n, c, G[1001], S[1001];

struct Conexao {
    int A, B;
    double dist;
};

bool cmp(Conexao X, Conexao Y) {
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
    vector<Conexao> pessoas, mst;
    vector<pii> p;
    pessoas.resize(124751), mst.resize(124751), p.resize(501);

    cin >> c;
    while (c--) {
        cin >> n;
        for (int i = 1; i <= n; i++)
            G[i] = i, S[i] = 1;

        unsigned tamanho = n * (n - 1) / 2;
        pessoas.clear(), mst.clear(), p.clear();

        for (int i = 1; i <= n; i++)
            cin >> p[i].first >> p[i].second;

        unsigned cont = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                pessoas[cont].A = i, pessoas[cont].B = j;
                pessoas[cont].dist = calcDist(p[i], p[j]);
                cont++;
            }
        }

        sort(pessoas.begin() + 1, pessoas.begin() + 1 + tamanho, cmp);
        cont = 0;
        for (int i = 1; i <= tamanho; i++) {
            if (Find(pessoas[i].A) != Find(pessoas[i].B)) {
                Union(pessoas[i].A, pessoas[i].B);
                mst[++cont] = pessoas[i];
            }
        }

        double ans = 0;
        for (int i = 1; i < n; i++)
            ans += mst[i].dist;
        ans /= 100;
        cout.precision(2);
        cout.setf(ios::fixed);
        cout << ans << "\n";
    }

    return 0;
}
