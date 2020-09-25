#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    unordered_map<int, int> counter;

    int t, n, h;
    cin >> t;
    while (t--)
    {
        cin >> n;

        for (int i = 20; i <= 230; i++) {
            counter[i] = 0;
        }

        for (int i = 0; i < n; i++) {
            cin >> h;
            counter[h]++;
        }

        bool hasPrinted = false;
        for (int i = 20; i <= 230; i++) {
            int total = counter[i];
            if (!total) continue;

            if (hasPrinted)
                cout << " ";
            else
                hasPrinted = true;
            cout << i;

            for (int j = 1; j < total; j++)
                cout << " " << i;
        }
        cout << "\n";
    }
    return 0;
}
