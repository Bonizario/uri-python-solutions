// Using vectors
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int dfs(const vector<vector<int>> &Vec, vector<int> &componente, int node) {
    stack<int> Stk;
    Stk.push(node);
    int semelhantes = 0;
    while (!Stk.empty()) {
        node = Stk.top();
        Stk.pop();
        for (int i = 0; i < Vec[node].size(); i++) {
            if (componente[Vec[node][i]] == -1) {
                Stk.push(Vec[node][i]);
                componente[Vec[node][i]] = componente[node];
                semelhantes++;
            }
        }
    }
    return semelhantes;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int i, n, m, a, b, pokemon, ans;
    vector<vector<int>> lista;
    vector<int> componente;
    lista.resize(1001);
    componente.resize(1001);

    while (cin >> n >> m) {
        for (i = 1; i <= n; i++)
            componente[i] = -1;

        for (i = 0; i < m; i++) {
            cin >> a >> b;
            lista[a].push_back(b);
            lista[b].push_back(a);
        }

        cin >> pokemon;
        componente[pokemon] = 1;
        ans = dfs(lista, componente, pokemon);
        cout << ans + 1 << "\n";

        for (i = 1; i <= n; i++)
            lista[i].clear();
        componente.clear();
    }

    return 0;
}

// Using arrays
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int dfs(const vector<int> *Vec, int *componente, int node) {
    stack<int> Stk;
    Stk.push(node);
    int semelhantes = 0;
    while (!Stk.empty()) {
        node = Stk.top();
        Stk.pop();
        for (int i = 0; i < Vec[node].size(); i++) {
            if (componente[Vec[node][i]] == -1) {
                Stk.push(Vec[node][i]);
                componente[Vec[node][i]] = componente[node];
                semelhantes++;
            }
        }
    }
    return semelhantes;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int i, n, m, a, b, pokemon, ans;
    vector<int> lista[1001];
    int componente[1001];

    while (cin >> n >> m) {
        for (i = 1; i <= n; i++)
            componente[i] = -1;

        for (i = 0; i < m; i++) {
            cin >> a >> b;
            lista[a].push_back(b);
            lista[b].push_back(a);
        }

        cin >> pokemon;
        componente[pokemon] = 1;
        ans = dfs(lista, componente, pokemon);
        cout << ans + 1 << "\n";

        for (i = 1; i <= n; i++)
            lista[i].clear();
    }

    return 0;
}


