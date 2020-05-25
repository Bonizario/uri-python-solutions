// MAXIMUM CONTIGNUS SUBARRAY SUM - KADANE'S ALGORITHM O(n)
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int maxSubarraySum(vector<int> V, int size) {
    int i, max_sum = V[0], current_sum = V[0];
    for (i = 1; i < size; i++) {
        current_sum = max(V[i], V[i] + current_sum);
        max_sum = max(max_sum, current_sum);
    }

    return max_sum;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int i, N, cost, profit, totalProfit;
    vector<int> V;

    while (cin >> N >> cost) {
        if (N == 0) {
            cout << "0\n";
            continue;
        }

        for (i = 0; i < N; i++) {
            cin >> profit;
            V.push_back(profit - cost);
        }

        totalProfit = maxSubarraySum(V, N);
        if (totalProfit <= 0) {
            cout << "0\n";
        } else {
            cout << totalProfit << "\n";
        }

        V.clear();
    }

    return 0;
}
