#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int i, j, di, dj, n, m;
    cin >> m >> n;

    char a[n][m];
    int visited[100][100];
    bool valid = false;

    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            cin >> a[i][j];
            visited[i][j] = 0;
        }
    }

    i = 0, j = 0, di = 0, dj = 0;
    while (true) {
        char current = a[i][j];
        if (current == '*') {
            valid = true;
            break;
        } else if (current == '>') {
            dj = 1;
            di = 0;
        } else if (current == '<') {
            dj = -1;
            di = 0;
        } else if (current == '^') {
            di = -1;
            dj = 0;
        } else if (current == 'v') {
            di = 1;
            dj = 0;
        }

        i += di, j += dj;
        if (visited[i][j] || i>= n || j >= m) break;
        visited[i][j] = 1;
    }

    cout << (valid ? "*\n" : "!\n");

    return 0;
}
