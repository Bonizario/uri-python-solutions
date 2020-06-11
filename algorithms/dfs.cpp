// componente[i] se trata da componente do vértice i
// inicialmente, componente[i] = -1 para todo vértice
// faremos a DFS como sendo uma função recursiva
// antes de chamar a DFS no primeiro nó, definimos sua componente
// RECURSIVO
#include <vector>
#define MAXN 50001

using namespace std;

int componente[MAXN];
vecto<int> vizinhos[MAXN];

void dfs(int x)
{
    for(int i = 0; i < (int)vizinhos[x].size(); i++)
    {
        int v = vizinhos[x][i];
        if (componente[v] == -1)
        {
            componente[v] = componente[x];
            dfs(v);
        }
    }
}

// STACK
#include <vector>
#include <stack>

using namespace std;

void dfs(const vector<vector<int>> & Vec, int s)
{
    stack<int> Stk;
    Stk.push(s);
    visited[s] = true;
    while (!Stk.empty())
    {
        int node = Stk.top();
        Stk.pop();
        for(int i = 0; i < Vec[node].size(); i++)
            if(!visited[Vec[node][i]])
            {
                Stk.push(Vec[node][i]);
                visited[Vec[node][i]] = true;
            }
    }
}
