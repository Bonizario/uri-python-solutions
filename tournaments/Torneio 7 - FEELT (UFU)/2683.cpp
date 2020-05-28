// 2683 - Union find with max and min
#include <iostream>
#include <algorithm>
#define MAXN 1000002

using namespace std;

struct tunel {
    int preco, entrada, saida;
};

bool maximo(tunel a, tunel b) {
    return a.preco > b.preco;
}

bool minimo(tunel a, tunel b) {
    return a.preco < b.preco;
}

tunel galeria[MAXN], mst[MAXN];

// union find
int pai[MAXN], peso[MAXN];

int find(int x) {
    if (x == pai[x]) return x;
    return pai[x] = find(pai[x]);
}

void join(int x, int y) {
    x = find(x);
    y = find(y);
    if (x == y) return;

    if (peso[x] < peso[y]) pai[x] = y;
    else if (peso[y] < peso[x]) pai[y] = x;
    else {
        pai[x] = y;
        peso[y]++;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int i, N, total;

    cin >> N;
        for (i = 1; i <= N; i++) {
        cin >> galeria[i].entrada >> galeria[i].saida >> galeria[i].preco;
        pai[i] = i;
        peso[i] = 0;
    }

    // MAX
    sort(galeria+1, galeria+1+N, maximo);

    int tamanho = 0;
    for (i = 1; i <= N; i++) {
        if (find(galeria[i].entrada) != find(galeria[i].saida)) {
            join(galeria[i].entrada, galeria[i].saida);
            mst[++tamanho] = galeria[i];
        }
    }

    total = 0;
    for (i = 1; i < N; i++) {
        total += mst[i].preco;
    }
    cout << total << "\n";

    // resetting union find arrays
    for (i = 1; i <= N; i++) {
        pai[i] = i;
        peso[i] = 0;
    }

    // MIN
    sort(galeria+1, galeria+1+N, minimo);

    tamanho = 0;
    for (i = 1; i <= N; i++) {
        if (find(galeria[i].entrada) != find(galeria[i].saida)) {
            join(galeria[i].entrada, galeria[i].saida);
            mst[++tamanho] = galeria[i];
        }
    }

    total = 0;
    for (i = 1; i < N; i++) {
        total += mst[i].preco;
    }
    cout << total << "\n";

    return 0;
}
