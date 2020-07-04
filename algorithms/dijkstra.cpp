#include <iostream>
#include <queue>
#include <vector>
#define MAXN 10100
#define INFINITO 999999999

using namespace std;

typedef pair<int, int> pii;

int n, m; // vertices, arestas
int cidade_noic; // cidade inicial
int cidade_succa; // cidade final
int distancia[MAXN]; // distâncias ao vértice inicial
int processado[MAXN]; // armazena se um vértice foi processado/fechado
vector<pii> vizinhos[MAXN]; // lista de adjacência, first => distância, second => vértice

void Dijkstra(int S) {
    for (int i = 1; i <= n; i++) {
        distancia[i] = INFINITO;
        processado[i] = false;
    }
    distancia[S] = 0;

    priority_queue<pii, vector<pii>, greater<pii>> pq;
    pq.push(pii(distancia[S], S));

    while (true) {
        int davez = -1;

        while (!pq.empty()) {
            int atual = pq.top().second;
            pq.pop();

            if (!processado[atual]) {  // ainda não foi fechado
                davez = atual;
                break;
            }
        }

        if (davez == -1) break;  // todos vértices foram fechados

        processado[davez] = true;

        for (int i = 0; i < (int)vizinhos[davez].size(); i++) {
            int dist = vizinhos[davez][i].first;
            int atual = vizinhos[davez][i].second;

            if (distancia[atual] > distancia[davez] + dist) {
                distancia[atual] = distancia[davez] + dist;
                pq.push(pii(distancia[atual], atual));
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

	cin >> n >> m;
	cin >> cidade_succa >> cidade_noic;

	for (int i = 1; i <= m; i++) {
		int x, y, tempo;
		cin >> x >> y >> tempo;
		// Em alguns exercícios o grafo NÃO é bidirecional!!
		vizinhos[x].push_back( pii(tempo, y) );
		vizinhos[y].push_back( pii(tempo, x) );
	}

	Dijkstra(cidade_succa);
	cout << distancia[cidade_noic] << "\n";

	return 0;
}
