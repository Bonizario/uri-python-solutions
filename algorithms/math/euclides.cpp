#include <bits/stdc++.h>
using namespace std;

int gcd(int x, int y) {
    return (y == 0 ? x : gcd(y, x % y));
}

// Python 3
/*
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x
*/
