#include <iostream>
#define MAXN 100001

using namespace std;

int parent[MAXN], weight[MAXN], quantity[MAXN];

int Find(int x) {
    while (x != parent[x]) {
        parent[x] = parent[parent[x]];  // path compression
        x = parent[x];
    }

    return x;
}

void Union(int x, int y) {
    x = Find(x);
    y = Find(y);

    if (x == y) return;

    if (weight[x] < weight[y]) {
        parent[x] = y;
        quantity[y] += quantity[x];
    } else if (weight[y] < weight[x]) {
        parent[y] = x;
        quantity[x] += quantity[y];
    } else {
        parent[y] = x;
        quantity[x] += quantity[y];
        weight[x]++;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    /* code */
    return 0;
}
