// componente[i] se trata da componente do vértice i
// inicialmente, componente[i] = -1 para todo vértice
// faremos a DFS como sendo uma função recursiva
// antes de chamar a DFS no primeiro nó, definimos sua componente
#define MAXN 50001
#include <vector>
using namespace std;

int componente[MAXN];
vector<int> vizinhos[MAXN];
// dfs com recursão
void dfs(int x) {  // vertice que vamos trabalhar

    for (int i = 0; i < (int)vizinhos[x].size(); i++) {

        int v = vizinhos[x][i];

        if (componente[v] == -1) {
            componente[v] = componente[x];
            dfs(v);
        }
    }
}

#include <vector>
#include <stack>
using namespace std;

int componente[MAXN];
vector<vector<int>> vizinhos;
// dfs com stack (antes de chamar, definimos a componente de 's')
void dfs(const vector<vector<int>> & Vec, int s) {
    stack<int> Stk;
    Stk.push(s);
    while (!Stk.empty()) {
        int node = Stk.top();
        Stk.pop();
        for (int i = 0; i < Vec[node].size(); i++) {
            if (componente[Vec[node][i]] == -1) {
                Stk.push(Vec[node][i]);
                componente[Vec[node][i]] = componente[node];
            }
        }
    }
}


void dfs(const vector<vector<int>> & Vec, int s) {
    std::stack<int> Stk;
    Stk.push(s);
    visited[s] = true;
    while (!Stk.empty()) {
        int Node = Stk.top();
        Stk.pop();
        cout << "Visited: " << Node << " ";
        for (int i = 0; i < Vec[Node].size(); i++) {
            if (!visited[Vec[Node][i]]) {
                Stk.push(Vec[Node][i]);
                visited[Vec[Node][i]] = true;
            }
        }

    }
}
