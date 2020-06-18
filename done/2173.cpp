// Solução estilo Felipe, com Union retornando um inteiro, sem array mst
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct Esquina {
    unsigned X, Y, C;
};

Esquina E[100001];

bool CmpCrescente(Esquina A, Esquina B) {
    return A.C < B.C;
}

bool CmpDecrescente(Esquina A, Esquina B) {
    return A.C > B.C;
}

// Union-Find
unsigned G[10001], S[10001];

unsigned Find(unsigned A) {
    if (G[A] == A) return A;
    return G[A] = Find(G[A]);
}

// ATENÇÃO, USE -1 EM EXERCÍCIOS QUE OS NÓS COMEÇAM EM 0
unsigned Union(unsigned A, unsigned B) {
    A = Find(A), B = Find(B);
    if (A == B)
        return 0;
    if (S[A] < S[B]) {
        G[A] = B;
        S[B] += S[A];
        return B;
    } else {
        G[B] = A;
        S[A] += S[B];
        return A;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    unsigned i, n, m;

    while (true) {
        cin >> n >> m;
        if (n == 0 && m == 0) break;

        for (i = 1; i <= n; i++) // USE NÚMERO DE NÓS E NÃO "M"
            G[i] = i, S[i] = 1;

        for (i = 1; i <= m; i++)
            cin >> E[i].X >> E[i].Y >> E[i].C;

        unsigned esq = 0, rouboMin = 0, rouboMax = 0;

        sort(E + 1, E + 1 + m, CmpCrescente);
        for (i = 1; i <= m; i++) {
            esq = Union(E[i].X, E[i].Y);
            if (esq) { // USE esq != -1 PARA EXERCÍCIOS QUE OS NÓS COMEÇAM EM 0
                rouboMin += E[i].C;
                if (S[esq] == n) break;
            }
        }

        // Limpando arrays do Union-Find
        for (i = 1; i <= n; i++) // USE NÚMERO DE NÓS E NÃO "M"
            G[i] = i, S[i] = 1;

        sort(E + 1, E + 1 + m, CmpDecrescente);
        for (i = 1; i <= m; i++) {
            esq = Union(E[i].X, E[i].Y);
            if (esq) {
                rouboMax += E[i].C;
                if (S[esq] == n) break;
            }
        }

        cout << rouboMax - rouboMin << "\n";
    }

    return 0;
}

// Solução estilo Neps, com array mst
/*
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct Esquina {
    unsigned X, Y, C;
};

bool CmpCrescente(Esquina A, Esquina B) {
    return A.C < B.C;
}

bool CmpDecrescente(Esquina A, Esquina B) {
    return A.C > B.C;
}

// Union-Find
unsigned G[10001], S[10001];

unsigned Find(unsigned A) {
    if (G[A] == A) return A;
    return G[A] = Find(G[A]);
}

void Union(unsigned A, unsigned B) {
    A = Find(A), B = Find(B);
    if (A == B) return;

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

    unsigned i, n, m;
    vector<Esquina> E, mst;

    while (true) {
        cin >> n >> m;
        if (n == 0 && m == 0) break;

        for (i = 1; i <= n; i++) // USE NÚMERO DE NÓS E NÃO "M"
            G[i] = i, S[i] = 1;

        E.clear(), E.resize(m + 1);
        mst.clear(), mst.resize(m + 1);

        for (i = 1; i <= m; i++)
            cin >> E[i].X >> E[i].Y >> E[i].C;

        unsigned tamanho = 0;
        sort(E.begin() + 1, E.end(), CmpCrescente);
        for (i = 1; i <= m; i++) {
            if (Find(E[i].X) != Find(E[i].Y)) {
                Union(E[i].X, E[i].Y);
                mst[++tamanho] = E[i];
            }
        }

        unsigned rouboMin = 0;
        for (i = 1; i < n; i++) {
            // cout<<mst[i].X<<" "<<mst[i].Y<<" "<<mst[i].C<<"\n";
            rouboMin += mst[i].C;
        }

        // Limpando arrays do Union-Find
        for (i = 1; i <= n; i++) // USE NÚMERO DE NÓS E NÃO "M"
            G[i] = i, S[i] = 1;

        tamanho = 0;
        sort(E.begin() + 1, E.end(), CmpDecrescente);
        for (i = 1; i <= m; i++) {
            if (Find(E[i].X) != Find(E[i].Y)) {
                Union(E[i].X, E[i].Y);
                // Colocar m no for acima ao invés de n falha no caso:
                // 3 2
                // 2 1 86
                // 1 3 34
                // 0 0
                // cout<<E[i].X<<" "<<E[i].Y<<" "<<E[i].C<<"\n";
                mst[++tamanho] = E[i];
            }
        }

        unsigned rouboMax = 0;
        for (i = 1; i < n; i++){
            // cout<<mst[i].X<<" "<<mst[i].Y<<" "<<mst[i].C<<"\n";
            rouboMax += mst[i].C;
        }

        cout << rouboMax - rouboMin << "\n";
    }

    return 0;
}
*/
