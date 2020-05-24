#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    unsigned short i, j, N;
    string name;
    double diff, score, scores[7], result;
    cin >> N;
    for (i = 0; i < N; i++) {
        result = 0;
        cin >> name;
        cin >> diff;
        for (j = 0; j < 7; j++) {
            cin >> scores[j];
        }
        sort(scores, scores + 7);
        for (j = 0; j < 7; j++) {
            if (j == 0 || j == 6) {
                continue;
            }
            result += scores[j];
        }
        result = result * diff;
        cout.precision(2);
        cout.setf(ios::fixed);
        cout << name << " " << result << "\n";
    }
    return 0;
}
