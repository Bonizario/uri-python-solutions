#include <iostream>
#include <algorithm>
#define MAXR 65
#define MAXC 205

using namespace std;

struct rot_cabo {
    int preco;
    int rot1, rot2;
};

bool comp(rot_cabo a, rot_cabo b) {
    return a.preco < b.preco;
}

// R: roteadores, C: cabos
rot_cabo cabo[MAXC];

// arvore
rot_cabo mst[MAXC];

// union find
int pai[MAXR], peso[MAXR];

int find(int x) {
    if (x == pai[x]) return x;
    return pai[x] = find(pai[x]);
}

void join(int x, int y) {
    x = find(x);
    y = find(y);

    if (peso[x] < peso[y]) pai[x] = y;
    else if (peso[y] < peso[x]) pai[y] = x;
    else {
        pai[x] = y;
        peso[y]++;
    }
}

int main() {
    int i, R, C;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> R >> C;

    for (i = 1; i <= C; i++)
        cin >> cabo[i].rot1 >> cabo[i].rot2 >> cabo[i].preco;

    for (i = 1; i <= R; i++)
        pai[i] = i;

    sort(cabo+1, cabo+1+C, comp);

    int tamanho = 0;
    for (i = 1; i <= C; i++) {
        if (find(cabo[i].rot1) != find(cabo[i].rot2)) {
            join(cabo[i].rot1, cabo[i].rot2);
            // faz diferença tamanho++ e ++tamanho
            mst[++tamanho] = cabo[i];
        }
    }

    int total = 0;
    for (i = 1; i < R; i++)
        total += mst[i].preco;

    cout << total << "\n";
    // for(i = 1; i < R; i++)
    //     cout << mst[i].rot1 << " " << mst[i].rot2 << " " << mst[i].preco << "\n";
    return 0;
}
