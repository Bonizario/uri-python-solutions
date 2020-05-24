#include <iostream>

using namespace std;

int main() {
    int N, desloc;
    string palavra;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> palavra;
        cin >> desloc;
        for (int i = 0; i < palavra.size(); i++) {
            if (palavra[i] - desloc >= 'A') {
                palavra[i] -= desloc;
            } else {
                palavra[i] += 26 - desloc;
            }
        }
        cout << palavra << "\n";
    }
    return 0;
}
