#include <iostream>

using namespace std;

int main() {
    unsigned short i, N, before, lower = 0;
    cin >> N;
    int v[N];
    for (i = 0; i < N; i++) {
        cin >> v[i];
        if (i == 0) {
            before = v[i];
            continue;
        }
        if (v[i] < before) {
            lower = i + 1;
            break;
        }
        before = v[i];
    }
    cout << lower << "\n";
}
