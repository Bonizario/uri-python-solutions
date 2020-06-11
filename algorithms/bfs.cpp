#include <vector>
#include <queue>

using namespace std;

void bfs(const vector<vector<int>> & Vec, int node)
{
    queue<int> Lst;
    Lst.push(node);
    visited[node] = true;
    while(!Lst.empty())
    {
        node = Lst.front();
        Lst.pop();
        for(int i = 0; i < Vec[node].size(); i++)
            if(!visited[Vec[node][i]])
            {
                Lst.push(Vec[node][i]);
                visited[Vec[node][i]] = true;
            }
    }
}
