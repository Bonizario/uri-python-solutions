#include <iostream>

using namespace std;

int main() {
    float matrix[12][12], result = 0;
    unsigned short i, j, C;
    char op;
    cin >> C;
    cin >> op;
    for (i = 0; i < 12; i++) {
        for (j = 0; j < 12; j++) {
            cin >> matrix[i][j];
        }
    }

    cout.precision(1);
    cout.setf(ios::fixed);
    if (op == 'S') {
        for (i = 0; i < 12; i++) {
            result += matrix[i][C];
        }
        cout << result << "\n";
    } else {
        for (i = 0; i < 12; i++) {
            result += matrix[i][C];
        }
        cout << result / 12 << "\n";
    }
    return 0;
}
