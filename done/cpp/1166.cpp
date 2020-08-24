#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<unsigned short> ages;
    unsigned short age, i, N;
    unsigned totalLetality;

    while (cin >> N) {
        for (i = 0; i < N; i++) {
            cin >> age;
            ages.push_back(age);
        }

        sort(ages.begin(), ages.end());
        totalLetality = 0;

        for (i = 0; i < N/2; i++) {
            totalLetality += ages[N - 1 - i] - ages[i];
        }

        cout << totalLetality << "\n";
        ages.clear();
    }
    return 0;
}
