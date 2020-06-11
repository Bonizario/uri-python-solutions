#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int dfs(const vector<vector<int>> & Vec, vector<int> & componente, int node)
{
    int i, movs = -1;
    stack<int> Stk;
    Stk.push(node);
    componente[node] = 1;
    while(!Stk.empty())
    {
        node = Stk.top();
        Stk.pop();
        movs++;
        for(i = 0; i < Vec[node].size(); i++)
            if(componente[Vec[node][i]] == -1)
            {
                Stk.push(Vec[node][i]);
                componente[Vec[node][i]] = componente[node];
                movs++;
            }
    }

    return movs;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int i, j, T, N, V, A, a, b;
    cin >> T;

    for(i = 0; i < T; i++)
    {
        cin >> N;
        cin >> V >> A;

        vector<int> componente;
        componente.resize(V);

        vector< vector<int> > lista;
        lista.resize(V);

        for(j = 0; j < V; j++)
            componente[j] = -1;

        for(j = 0; j < A; j++)
        {
            cin >> a >> b;
            lista[a].push_back(b);
            lista[b].push_back(a);
        }

        int ans;
        ans = dfs(lista, componente, N);
        cout << ans << "\n";

        for(j = 0; j < V; j++)
            lista[j].clear();
        componente.clear();
    }

    return 0;
}
