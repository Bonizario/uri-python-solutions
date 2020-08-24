// 2782 - Escadinha
#include <iostream>

using namespace std;

int main() {
    int i, N;
    cin >> N;
    int sequence[N];
    for (i = 0; i < N; i++) {
        cin >> sequence[i];
    }

    int before, now, stepladders;
    if (N == 1 || N == 2) {
        cout << 1 << endl;
    } else {
        stepladders = 1;
        before = sequence[0] - sequence[1];
        for (i = 2; i < N; i++) {
            now = sequence[i - 1] - sequence[i];
            if (now != before) { // no need to update before if they're equal
                before = now;
                stepladders++;
            }
        }
        cout << stepladders << endl;
    }
    return 0;
}
