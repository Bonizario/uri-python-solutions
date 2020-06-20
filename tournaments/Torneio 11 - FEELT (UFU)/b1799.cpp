#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#define INFINITO 999999999

using namespace std;

typedef pair<int, int> pii;

unordered_map<string, int> conversor;

int n, m;
int entrada, saida, queijo;
int distancia[4001];
int processado[4001];
vector<pii> vizinhos[4001];
priority_queue<pii, vector<pii>, greater<pii>> fila;

void Dijkstra(int S) {
    while (!fila.empty())
        fila.pop();

    for (int i = 1; i <= n; i++) {
        processado[i] = false;
        distancia[i] = INFINITO;
    }

    distancia[S] = 0;
    fila.push(pii(distancia[S], S));

    while (true) {
        int davez = -1;

        while (!fila.empty()) {
            int atual = fila.top().second;
            fila.pop();

            if (!processado[atual]) {
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

    cin >> n >> m;

    string a, b;
    int contador = 1, A, B;
    for (int i = 1; i <= m; i++) {
        cin >> a >> b;
        if (conversor.find(a) == conversor.end())
            conversor[a] = contador++;
        if (conversor.find(b) == conversor.end())
            conversor[b] = contador++;

        A = conversor[a];
        B = conversor[b];

        vizinhos[A].push_back(pii(1, B)); // peso sempre 1
        vizinhos[B].push_back(pii(1, A));
    }

    /*
    for (auto key : conversor)
        cout << key.first << " " << key.second << " ";
    cout << "\n";
    */

    entrada = conversor["Entrada"];
    queijo = conversor["*"];
    saida = conversor["Saida"];

    Dijkstra(entrada);
    int entrada_queijo = distancia[queijo];

    Dijkstra(queijo);
    int queijo_saida = distancia[saida];

    //cout << "\n\n" << entrada_queijo << " " << queijo_saida << "\n";
    cout << entrada_queijo + queijo_saida << "\n";

    return 0;
}
