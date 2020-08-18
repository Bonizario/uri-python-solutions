/*
    Union-find algorithm used with the disjointed-set data structure
    and Kruskal's algorithm.
*/

#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e5;

int G[MAXN], S[MAXN]; // Union by size

// Recursive
int Find(int A) {
    if (G[A] == A)
        return A;
    return G[A] = Find(G[A]); // Path compression
}

// Iterative
int Find(int A) {
    while (G[A] != A) {
        G[A] = G[G[A]]; // Path compression
        A = G[A];
    }
    return A;
}

void Union(int A, int B) {
    A = Find(A), B = Find(B);

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
