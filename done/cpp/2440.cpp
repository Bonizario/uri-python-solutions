// Solution with recursive dfs and iterative dfs (with stack container)
#include <iostream>
#include <vector>
#define MAXN 50001

using namespace std;

int n, m;
int componente[MAXN];
vector<int> lista[MAXN];

void dfs(int x) {
    for (int i = 0; i < (int)lista[x].size(); i++) {
        int v = lista[x][i];

        if (componente[v] == -1) {
            componente[v] = componente[x];
            dfs(v);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;

    for (int i = 1; i <= n; i++)
        componente[i] = -1;

    int a, b;
    for (int i = 1; i <= m; i++) {
        cin >> a >> b;
        lista[a].push_back(b);
        lista[b].push_back(a);
    }

    int numero_componentes = 0;
    for (int i = 1; i <= n; i++) {
        if (componente[i] == -1) {  // i não tem componente
            componente[i] = ++numero_componentes;

            dfs(i);
        }
    }

    cout << numero_componentes << "\n";

    return 0;
}

//-----------------------------------------------------------------------------------//
// Using stack without global vectors
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

void dfs(const vector<vector<int>>&Vec, vector<int>&componente, int s) {
    stack<int> Stk;
    Stk.push(s);
    while (!Stk.empty()) {
        int node = Stk.top();
        Stk.pop();
        for (int i = 0; i < Vec[node].size(); i++) {
            if (componente[Vec[node][i]] == -1) {
                Stk.push(Vec[node][i]);
                componente[Vec[node][i]] = componente[s];
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> lista;
    lista.resize(n+1);
    vector<int> componente;
    componente.resize(n+1);

    for (int i = 1; i <= n; i++)
        componente[i] = -1;

    int a, b;
    for (int i = 1; i <= m; i++) {
        cin >> a >> b;
        lista[a].push_back(b);
        lista[b].push_back(a);
    }

    int numero_componentes = 0;
    for (int i = 1; i <= n; i++) {
        if (componente[i] == -1) {
            componente[i] = ++numero_componentes;

            dfs(lista, componente, i);
        }
    }
    cout << numero_componentes << "\n";

    return 0;
}

//-----------------------------------------------------------------------------------//
// Using stack with global vectors
#include <iostream>
#include <vector>
#include <stack>
#define MAXN 50001

using namespace std;

int n, m;
int componente[MAXN];
vector<int> lista[MAXN];

void dfs(int s) {
    stack<int> Stk;
    Stk.push(s);
    while (!Stk.empty()) {
        int node = Stk.top();
        Stk.pop();
        for (int i = 0; i < (int)lista[node].size(); i++) {
            if (componente[lista[node][i]] == -1) {
                Stk.push(lista[node][i]);
                componente[lista[node][i]] = componente[s];
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;
    for (int i = 1; i <= n; i++)
        componente[i] = -1;

    int a, b;
    for (int i = 1; i <= m; i++) {
        cin >> a >> b;
        lista[a].push_back(b);
        lista[b].push_back(a);
    }

    int numero_componentes = 0;
    for (int i = 1; i <= n; i++) {
        if (componente[i] == -1) {
            componente[i] = ++numero_componentes;
            dfs(i);
        }
    }
    cout << numero_componentes << "\n";

    return 0;
}

