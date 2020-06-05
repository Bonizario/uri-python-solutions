#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool compare(pair<int,int> a, pair<int,int> b) {
    if (a.first != b.first) return a.first > b.first;
    return a.second < b.second;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int A, V, i, id1, id2, test = 1;
    vector< pair<int,int> > airports;

    while (true) {
        cin >> A >> V;

        if (A == 0 && V == 0) break;
        cout << "Teste " << test++ << "\n";

        for (i = 1; i <= A; i++)
            airports.push_back(make_pair(0, i));

        for (i = 1; i <= V; i++) {
            cin >> id1 >> id2;
            airports[id1-1].first++;
            airports[id2-1].first++;
        }

        sort(airports.begin(), airports.end(), compare);

        for (i = 0; i < A; i++) {
            cout << airports[i].second << " ";

            if (airports[i].first != airports[i+1].first)
                break;
        }

        cout << "\n\n";
        airports.clear();
    }

    return 0;
}
