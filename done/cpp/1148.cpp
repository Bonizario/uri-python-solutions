#include <bits/stdc++.h>
#define MAXN 501
#define INF 1e9
using namespace std;

typedef pair<int, int> pii;

int n, e, x, y, h, k;
int dist[MAXN];
bool visited[MAXN];
vector<pii> adj[MAXN];
bool ok[MAXN][MAXN];

void dijkstra(int S) {
    for (int i = 1; i <= n; i++)
        dist[i] = INF, visited[i] = false;
    dist[S] = 0;

    priority_queue<pii, vector<pii>, greater<pii>> pq;
    pq.push(pii(0, S));

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        if (visited[u]) continue;
        visited[u] = true;

        for (auto V: adj[u]) {
            int v = V.second, w = V.first;
            if (ok[u][v] && ok[v][u]) { // LAZY FIX TO AVOID RE-IMPLEMENTATION WITH ADJ MATRIX INSTEAD OF ADJ LIST
                dist[v] = min(dist[u], dist[v]);
                pq.push(pii(dist[v], v));
            }
            else if (dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
                pq.push(pii(dist[v], v));
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    while (true) {
        cin >> n >> e;
        if (n == 0 && e == 0) break;
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                ok[i][j] = false;

        for (int i = 1; i <= n; i++)
            adj[i].clear();

        for (int i = 1; i <= e; i++) {
            cin >> x >> y >> h;
            adj[x].push_back(pii(h, y));
            ok[x][y] = true;
        }

        cin >> k;
        for (int i = 1; i <= k; i++) {
            cin >> x >> y;
            dijkstra(x);
            if (dist[y] != INF) {
                cout << dist[y] << "\n";
            } else {
                cout << "Nao e possivel entregar a carta\n";
            }
        }

        cout << "\n";
    }

    return 0;
}
