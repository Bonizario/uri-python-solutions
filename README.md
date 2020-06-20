<p align="center">
  <img alt="URI" title="URI" src="assets/uri-logo.png">
</p>

<h2 align="center">URI Online Judge is a project that is being developed by the Computer Science Department of URI University</h2>

<h3 align="center">The main goal of the project is to provide programming practice and knowledge sharing</h3>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/Bonizario/be-the-hero?color=d61635">

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

<h3>🐍 2020 ICPC World Finals - Python 3 <a href="https://github.com/Bonizario/uri-solutions/raw/master/assets/WF2020.pypy3.modules.pdf" target="_blank">Installed Modules</a></h3>

## :octocat: Algorithms

### Union-Find / Disjoint-Set data structure
```cpp
#include <bits/stdc++.h>
using namespace std;

#define MAXN 100000

int G[MAXN], S[MAXN];

int Find(int A) {
    if (G[A] == A) return A;
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
```

### Depth-First Search

```cpp
#include <bits/stdc++.h>
using namespace std;

#define MAXN 100000

int component[MAXN];
vector<int> siblings;

void DFS(int node) {
    for (int i = 0; i < (int)siblings[node].size(); i++) {
        int s = siblings[node][i];

        if (component[v] == -1) {
            component[v] = component[node];
            DFS(v);
        }
    }
}

int main() {
    int N, M; // nodes, edges
    cin >> N >> M;

    for (int i = 1; i <= N; i++)
        component[i] = -1;

    int A, B; // adjacency list
    for (int i = 1; i <= M; i++) {
        cin >> A >> B;
        siblings[A].push_back(B);
        siblings[B].push_back(A);
    }

    // code [...]

    return 0;
}
```
