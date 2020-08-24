// 2425 - Banco

// LÓGICA I
// Nessa lógica, armazeno o tempo de saída na primeira posição do pair
// E o tempo de chegada na segunda posição. Primeiro da fila é o menor valor!
// Assim, o primeiro da fila será o cliente que sai mais rapidamente.
// Desempate ocorre com a segunda posição do pair, ou seja, quem chegou primeiro (menor valor).

#include <iostream>
#include <queue>

using namespace std;

typedef pair<int, int> pii;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    priority_queue<pii, vector<pii>, greater<pii>> pq;
    int i, C, N, chegada, duracao, espera, esperaram = 0;
    pii cliente;

    cin >> C >> N;

    for (i = 0; i < C; i++)  // preenchendo os caixas
        pq.push(pii(0, 0));

    for (i = 0; i < N; i++) {
        cin >> chegada >> duracao;
        cliente = pq.top();
        pq.pop();

        espera = cliente.first - chegada;
        if (espera > 20)
            esperaram++;

        //cout << "Espera de "<<chegada<<" "<<duracao<<" eh="<<espera<<"\n";

        if (espera >= 0)
            pq.push(make_pair(cliente.first + duracao, chegada));
        else // chegou muito depois do último cliente ser atendido, espera negativa
            pq.push(make_pair(chegada + duracao, chegada));

        //cout << "Depois "<<cliente.first + duracao<<" "<<chegada<<"\n\n";
    }

    cout << esperaram << "\n";

    return 0;
}


// LÓGICA II
// Nessa versão, armazeno o início do atendimento do cliente na primeira posição,
// e a duração desse atendimento na segunda posição.
// A pq é ordenada com uma função personalizada, de maneira que o cliente que
// desocupar primeiro é sempre o primeiro da fila.

#include <iostream>
#include <queue>

using namespace std;

typedef pair<int, int> pii;

struct cmp {  // LEMBRE DE COLOCAR bool ANTES DE operator!
    bool operator()(const pii &a, const pii &b) {
        return (a.first + a.second) > (b.first + b.second);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int i, c, n;
    cin >> c >> n;

    priority_queue<pii, vector<pii>, cmp> pq;
    for (i = 0; i < c; i++)  // preenchendo os caixas
        pq.push(pii(0, 0));

    pii cliente;
    int chegada, duracao, espera, esperaram = 0;
    for (i = 0; i < n; i++) {
        cin >> chegada >> duracao;
        cliente = pq.top();
        pq.pop();
        espera = cliente.first + cliente.second - chegada;
        if (espera > 20)
            esperaram++;

        if (espera >= 0)
            pq.push(pii(cliente.first + cliente.second, duracao));
        else
            pq.push(pii(chegada, duracao));
    }

    cout << esperaram << "\n";

    return 0;
}
