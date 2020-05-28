#include <iostream>
#include <queue>
#include <functional>  // std::greater<pair<int,int>>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    pair<int, int> vendedor;
    int i, tempo, N, L;

    cin >> N >> L;

    int ligacoes[N];
    for (i = 1; i <= N; i++) {
        pq.push(make_pair(0, i));
        ligacoes[i] = 0;
    }

    for (i = 0; i < L; i++) {
        cin >> tempo;
        vendedor = pq.top();
        pq.pop();
        pq.push(make_pair(vendedor.first + tempo, vendedor.second));
        ligacoes[vendedor.second]++;
    }

    for (i = 1; i <= N; i++)
        cout << i << " " << ligacoes[i] << "\n";

    return 0;
}
