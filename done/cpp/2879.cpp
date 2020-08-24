// 2879 - Desvendando Monty Hall
#include <iostream>

using namespace std;

int main() {
    int N, door, wins = 0;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> door;
        if (door == 2 || door == 3) {
            wins++;
        }
    }
    cout << wins << endl;
    return 0;
}
