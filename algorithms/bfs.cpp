#include <vector>
#include <queue>
#define MAXN 100000

using namespace std;

bool visited[MAXN];

void bfs(const vector<vector<int>> &Vec, int node) {
    queue<int> Lst;
    Lst.push(node);
    visited[node] = true;

    while (!Lst.empty()) {
        node = Lst.front();
        Lst.pop();

        for (int i = 0; i < Vec[node].size(); i++) {
            if (!visited[Vec[node][i]]) {
                visited[Vec[node][i]] = true;
                Lst.push(Vec[node][i]);
            }
        }
    }
}
