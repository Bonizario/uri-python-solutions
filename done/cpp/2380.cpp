#include <iostream>
#define MAXN 100002

using namespace std;

int pai[MAXN], peso[MAXN];

int find(int x) {
    if (x == pai[x]) return x;
    return pai[x] = find(pai[x]);
}

void join(int x, int y) {
    x = find(x);
    y = find(y);

    if (x == y) return;

    if (peso[x] > peso[y]) {
        pai[y] = x;
    } else if (peso[x] < peso[y]) {
        pai[x] = y;
    } else {
        pai[x] = y;
        peso[y]++;
    }
}

int main() {
    char op;
    int i, N, B, banco1, banco2;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> B;

    for (i = 1; i <= N; i++) {
        pai[i] = i;
    }

    for (i = 1; i <= B; i++) {
        cin >> op >> banco1 >> banco2;
        if (op == 'F') {
            join(banco1, banco2);
        } else {
            if (find(banco1) == find(banco2)) {
                cout << "S\n";
            } else {
                cout << "N\n";
            }
        }
    }

    return 0;
}
