#include <iostream>
#include <queue>
#include <functional>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    int i, C, N, chegada, duracao, espera, esperaram = 0;
    pair<int,int> cliente;

    cin >> C >> N;

    for (i = 0; i < C; i++)
        pq.push(make_pair(0, 0));

    for (i = 0; i < N; i++) {
        cin >> chegada >> duracao;
        cliente = pq.top();
        pq.pop();

        espera = cliente.first - chegada;
        if (espera > 20)
            esperaram++;
        // priority queue é estável, ou seja, dois clientes
        // que chegam em um mesmo tempo
        // permanecem na ordem em que chegaram após a inserção na queue

        // invertemos para a ordem ser correta. 0 10 demora mais que 1 1
        // logo, 1 1 deve ficar na frente, mas na ordem convencional 0 > 1!
        if (espera >= 0)
            pq.push(make_pair(cliente.first + duracao, chegada));
        else
            pq.push(make_pair(chegada + duracao, chegada));
    }

    cout << esperaram << "\n";

    return 0;
}
