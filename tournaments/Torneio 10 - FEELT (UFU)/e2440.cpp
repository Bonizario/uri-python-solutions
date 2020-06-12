#include <iostream>
#include <vector>
#include <stack>

using namespace std;

void dfs(const vector<vector<int>> & Vec, vector<int> &componente, int node) {
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

    int i, n, m, a, b, ans = 0;
    cin >> n >> m;

    vector<vector<int>> lista;
    lista.resize(n+1);
    vector<int> componente;
    componente.resize(n+1);

    for (i = 1; i <= n; i++)
        componente[i] = -1;

    for (i = 1; i <= m; i++) {
        cin >> a >> b;
        lista[a].push_back(b);
        lista[b].push_back(a);
    }

    for (i = 1; i <= n; i++) {
        if (componente[i] == -1) {
            componente[i] = ++ans;
            dfs(lista, componente, i);
        }
    }

    cout << ans << "\n";

    return 0;
}
