/*
    Time Complexity: O(ElogV), E <= V^2
*/

#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;

const int MAXN = 1e5;
const int INF = 1e9;

int n, m; // Nodes and Edges
int dist[MAXN]; // Current distance in each node
bool visited[MAXN]; // Visited nodes
vector<pii> adj[MAXN]; // Adjacency list graph

void dijkstra(int S) {
    // First part of the algorithm
    for (int i = 1; i <= n; i++)
        dist[i] = INF;
    dist[S] = 0;

    // Priority queue to store the current distances in ascending order
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    // Initially, insert the root
    pq.push(pii(0, S));

    // When all nodes are visited, the queue is empty and the algorithm ends
    while (!pq.empty()) {
        // Second part of the algorithm
        int u = pq.top().second;
        pq.pop();

        // Ignore visited nodes
        if (visited[u])
            continue;

        // Mark the current node
        visited[u] = true;

        for (auto V : adj[u]) {
            int v = V.second, w = V.first;

            // Third part of the algorithm
            if (dist[v] > dist[u] + w) {
                // Update the current distance of V and put it in the queue
                dist[v] = dist[u] + w;
                pq.push(pii(dist[v], v));
            }
        }
    }
}
