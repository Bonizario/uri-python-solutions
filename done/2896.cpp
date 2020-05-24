// 2896 - Aproveite a Oferta
#include <iostream>

using namespace std;

int main() {
    int T, N, K, total, rest;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N >> K;
        total = N / K;
        rest = N % K;
        cout << total + rest << endl;
    }
    return 0;
}
