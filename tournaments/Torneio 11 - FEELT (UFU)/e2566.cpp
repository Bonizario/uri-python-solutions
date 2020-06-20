#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#define INFINITO 999999999;

using namespace std;

typedef pair<int, int> pii;

int n, m;
int distancia[101];
bool processado[101];
priority_queue<pii, vector<pii>, greater<pii>> fila;

void Dijkstra(int S, const vector<vector<pii>> &vizinhos) {
    while (!fila.empty())
        fila.pop();

    for (int i = 1; i <= n; i++) {
        distancia[i] = INFINITO;
        processado[i] = false;
    }

    distancia[S] = 0;
    fila.push(pii(distancia[S], S));

    while (true) {
        int davez = -1;

        while (!fila.empty()) {
            int atual = fila.top().second;
            fila.pop();

            if(!processado[atual]) {
                davez = atual;
                break;
            }
        }

        if (davez == -1) break;

        processado[davez] = true;

        for (int i = 0; i < (int)vizinhos[davez].size(); i++) {
            int dist = vizinhos[davez][i].first;
            int atual = vizinhos[davez][i].second;

            if (distancia[atual] > distancia[davez] + dist) {
                distancia[atual] = distancia[davez] + dist;
                fila.push(pii(distancia[atual], atual));
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<vector<pii>> vizinhos0; // onibus
    vector<vector<pii>> vizinhos1; // aviao
    vizinhos0.resize(101);
    vizinhos1.resize(101);
    int a, b, t, r;

    while (cin >> n >> m) {
        for (int i = 0; i <= 100; i++)
            vizinhos0[i].clear(), vizinhos1[i].clear();

        for (int i = 1; i <= m; i++) {
            cin >> a >> b >> t >> r;
            if (t == 1)
                vizinhos1[a].push_back(pii(r, b));
            else
                vizinhos0[a].push_back(pii(r, b));
        }

        Dijkstra(1, vizinhos0);
        int dist0 = distancia[n];

        Dijkstra(1, vizinhos1);
        int dist1 = distancia[n];

        cout << (dist0 < dist1 ? dist0 : dist1) << "\n";
    }

    return 0;
}
