#include <iostream>
#include <vector>
#include <stack>

using namespace std;

void dfs(const vector<vector<int>> &Vec, vector<int> &componente, int node) {
    stack<int> Stk;
    Stk.push(node);
    while (!Stk.empty()) {
        node = Stk.top();
        Stk.pop();
        for (int i = 0; i < Vec[node].size(); i++) {
            if (componente[Vec[node][i]] == -1) {
                Stk.push(Vec[node][i]);
                componente[Vec[node][i]] = componente[node];
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int i, j, t, n, m;
    cin >> t;
    for (i = 1; i <= t; i++) {
        cin >> n >> m;

        vector<vector<int>> lista;
        lista.resize(n+1);
        vector<int> componente;
        componente.resize(n+1);

        for (j = 1; j <= n; j++)
            componente[j] = -1;

        int a, b;
        for (j = 0; j < m; j++) {
            cin >> a >> b;
            lista[a].push_back(b);
            lista[b].push_back(a);
        }

        int ans = 0;
        for (j = 1; j <= n; j++) {
            if (componente[j] == -1) {
                componente[j] = ++ans;
                dfs(lista, componente, j);
            }
        }

        cout << "Caso #" << i << ": ";
        if (ans == 1)
            cout << "a promessa foi cumprida\n";
        else
            cout << "ainda falta(m) " << ans - 1 << " estrada(s)\n";

        for (j = 1; j <= n; j++)
            lista[j].clear();
        componente.clear();
    }

    return 0;
}
