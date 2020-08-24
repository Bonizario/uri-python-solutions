#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compareSkills(pair<unsigned, string> a, pair<unsigned, string> b) {
    return a.first > b.first;
}

bool compareNames(pair<unsigned, string> a, pair<unsigned, string> b) {
    return a.second < b.second;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    unsigned short i, j, N, T;
    vector< pair<unsigned, string> > players;
    pair<unsigned, string> player;

    cin >> N >> T;
    for (i = 0; i < N; i++) {
        cin >> player.second >> player.first;
        players.push_back(player);
    }
    sort(players.begin(), players.end(), compareSkills);

    unsigned counter = 0;
    vector< vector< pair<unsigned, string> > > teams;
    for (i = 0; i < T; i++) {
        teams.push_back({});
    }

    for (i = 0; i < N; i++) {
        teams[counter].push_back(players[i]);
        counter++;
        if (counter == T) {
            counter = 0;
        }
    }

    for (i = 0; i < T; i++) {
        cout << "Time " << i + 1 << "\n";
        sort(teams[i].begin(), teams[i].end(), compareNames);
        for (j = 0; j < (unsigned)teams[i].size(); j++) {
            cout << teams[i][j].second << "\n";
        }
        cout << "\n";
    }

    return 0;
}
