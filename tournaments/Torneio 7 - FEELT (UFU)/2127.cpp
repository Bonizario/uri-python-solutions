#include <iostream>
#include <algorithm>
#define MAXN 1001

using namespace std;

// Defining cipo struct
typedef struct _cipo {
    short unsigned u, v, c;
} t_cipo;

// sort in ascending order by cost
bool compara(t_cipo a, t_cipo b) {
    return a.c < b.c;
}

// Union Find functions
short unsigned Parent[MAXN], Size[MAXN];

short unsigned Find(short unsigned x) {
    while (Parent[x] != x) {
        Parent[x] = Parent[Parent[x]];
        x = Parent[x];
    }

    return x;
}

short unsigned Union(short unsigned a, short unsigned b) {
    short unsigned A = Find(a);  // set of a
    short unsigned B = Find(b);  // set of b

    if (A == B)
        return 0;

    if (Size[A] < Size[B]) {
        Size[B] += Size[A];
        Parent[A] = B;
        return B;
    } else {
        Size[A] += Size[B];
        Parent[B] = A;
        return A;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    short unsigned u, v, c, N;
    unsigned i, k = 1, custo, M;

    cin >> N >> M;
    while (!cin.eof()) {
        // union find setup
        for (i = 1; i <= N; i++) {
            Parent[i] = i;
            Size[i] = 1;
        }

        // reading input, starts from index 0
        t_cipo C[M];

        for (i = 0; i < M; i++)
            cin >> C[i].u >> C[i].v >> C[i].c;

        sort(C, C + M, compara);

        custo = 0;
        short unsigned g;
        for (i = 0; i < M; i++) {
            g = Union(C[i].u, C[i].v);
            if (g) { // they are not equal
                custo += C[i].c;
                if (Size[g] == N) break;
            }
        }

        cout << "Instancia " << k++ << "\n";
        cout << custo << "\n\n";

        cin >> N >> M;
    }

    return 0;
}
