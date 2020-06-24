<p align="center">
  <img alt="URI Online Judge" title="URI Online Judge" src="assets/uri-logo.png">
</p>

<h2 align="center">The main goal of URI is to provide programming practice and knowledge sharing</h3>

<h3 align="center">Their platform contains more than 2000 problems divided in 9 categories, here are some Python 3 and C++ solutions that I developed</h2>

<br />

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/Bonizario/uri-solutions?color=d61635">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/bonizario/uri-solutions?color=d81f34">

  <a href="https://www.linkedin.com/in/gabriel-bonizario/">
    <img alt="Made by gabriel-bonizario" src="https://img.shields.io/badge/made%20by-gabriel%20bonizario-dc2c34">
  </a>

  <a href="https://github.com/bonizario/ecoleta/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/bonizario/uri-solutions?color=e54034">
  </a>

  <a href="https://github.com/Bonizario/ecoleta/blob/master/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/bonizario/uri-solutions?color=f0442c">
  </a>

  <a href="https://github.com/Bonizario/be-the-hero/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/bonizario/uri-solutions?style=social">
  </a>
</p>

<br />
<br />

# :books: Algorithms

## Graph Representation - Adjacency List

```cpp
#include <bits/stdc++.h>
using namespace std;

#define MAXN 50000 // Nodes

vector<int> adj[MAXN];

int main() {
    int N, M; // Nodes, Edges
    cin >> N >> M;

    int A, B;
    for (int i = 1; i <= M; i++) {
        cin >> A >> B;
        adj[A].push_back(B);
        adj[B].push_back(A);
    }

    // Code [...]

    return 0;
}
```

<br />

## Depth-First Search

```cpp
#include <bits/stdc++.h>
using namespace std;

#define MAXN 50000 // Nodes

int component[MAXN]; // Set everything to -1 in main()
vector<int> adj[MAXN]; // Adjacency list

// Change component[node] before calling the DFS

// Recursive
void DFS(int node) {
    for (int i = 0; i < (int)adj[node].size(); i++) {
        int v = adj[node][i];

        if (component[v] == -1) {
            component[v] = component[node];
            DFS(v);
        }
    }
}

// Iterative
void DFS(int node) {
    stack<int> Stk;
    Stk.push(node);

    while (!Stk.empty()) {
        node = Stk.top();
        Stk.pop();
        for (int i = 0; i < (int)adj[node].size(); i++) {
            int v = adj[node][i];

            if (component[v] == -1) {
                component[v] = component[node];
                Stk.push(v);
            }
        }
    }
}
```

<br />

## Breadth-First Search

```cpp
#include <bits/stdc++.h>
using namespace std;

#define MAXN 100000

int component[MAXN]; // Set everything to -1 in main()
vector<int> adj[MAXN]; // Adjacency list

// Change component[node] before calling the BFS

void BFS(int node) {
    queue<int> Lst;
    Lst.push(node);

    while (!Lst.empty()) {
        node = Lst.front();
        Lst.pop();
        for (int i = 0; i < (int)adj[node].size(); i++) {
            int v = adj[node][i];

            if (component[v] == -1) {
                component[v] = component[node];
                Lst.push(v);
            }
        }
    }
}
```

<br />

## Union-Find / Disjoint-Set data structure

```cpp
#include <bits/stdc++.h>
using namespace std;

#define MAXN 100000

int G[MAXN], S[MAXN]; // Parents, Sizes

// Recursive
int Find(int A) { 
    if (G[A] == A)
        return A;
    return G[A] = Find(G[A]);
}

// Iterative
int Find(int A) {
    while (G[A] != A) {
        G[A] = G[G[A]];
        A = G[A];
    }
    return A; 
}

int Union(int A, int B) {
    A = Find(A);
    B = Find(B);

    if (A == B)
        return;
    if (S[A] < S[B]) {
        G[A] = B;
        S[B] += S[A];
    } else {
        G[B] = A;
        S[A] += S[B];
    }
}
```

<br />

## Kruskal

```cpp
#include <bits/stdc++.h>
using namespace std;

#define MAXN 50000 // Nodes
#define MAXM 100000 // Edges

struct t_edge {
    int X, Y, W; // Node X, Node Y and Edge Weight
};

bool cmp(t_edge A, t_edge B) {
    return A.W < B.W; // Ascending order
}

// Edges and Minimum Spanning Tree
t_edge Edge[MAXM], MST[MAXM];

// Union-Find Functions
int G[MAXN], S[MAXN];

int Find(int A) { 
    if (G[A] == A)
        return A;
    return G[A] = Find(G[A]);
}

int Union(int A, int B) {
    A = Find(A);
    B = Find(B);

    if (A == B)
        return -1;
    if (S[A] < S[B]) {
        G[A] = B;
        S[B] += S[A];
        return B;
    } else {
        G[B] = A;
        S[A] += S[B];
        return A;
    }
}

int main() {
    int N, M;
    cin >> N >> M;

    for (int i = 0; i < N; i++)
        G[i] = i, S[i] = 1;

    for (int i = 0; i < M; i++)
        cin >> Edge[i].X >> Edge[i].Y >> Edge[i].W;

    sort(Edge, Edge + M, cmp);

    int cont = 0;
    for (int i = 0; i < M; i++) {
        int E = Union(Edge[i].X, Edge[i].Y);

        // Do not add them to the MST if they are children of the same parent
        if (E != -1) { 
            MST[cont++] = Edge[i];
            if (S[E] == N) break;
        }
    }

    int result = 0;
    for (int i = 0; i < cont; i++) {
        cout << MST[i].X << " " << MST[i].Y << " " << MST[i].W << "\n";
        result += MST[i].W;
    }

    cout << result << "\n";

    return 0;
}
```

<br />

## Binary Search

```cpp
#include <bits/stdc++.h>
using namespace std;

int BinarySearch(int arr[], int target, int N) {
    int mid, L = 0, R = N - 1;

    while (L <= R) {
        mid = L + (R - L) / 2;

        if (arr[mid] == target)
            return mid;
        if (arr[mid] < target)
            L = mid + 1;
        else
            R = mid - 1;        
    }

    return -1;
}
```

<br />

# :postbox: Contato

Desenvolvido por **Gabriel Bonizário** 👋🏻

**Linkedin**: [gabriel-bonizario](https://www.linkedin.com/in/gabriel-bonizario/)

**Email**: gabrielbonizario98@gmail.com

---
