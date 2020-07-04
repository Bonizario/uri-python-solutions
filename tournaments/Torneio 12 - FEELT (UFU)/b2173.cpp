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
        if (n == 0 && m == 0)
            break;

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
                // if (S[esq] == n) break;
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
                // if (S[esq] == n) break;
            }
        }

        cout << rouboMax - rouboMin << "\n";
    }

    return 0;
}
