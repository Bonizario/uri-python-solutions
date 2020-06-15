#include <iostream>
#include <unordered_map>

using namespace std;

unordered_map<string, int> dict;

int G[10000], S[10000];
pair<int,int> skills[10000];

int Find(int a) {
    if (G[a] == a) return a;
    return G[a] = Find(G[a]);
}

void Union(int a, int b) {
    int A = Find(a);
    int B = Find(b);

    if (A == B) return;
    if (skills[a].first>5 || skills[b].first>5 ||
        skills[A].second == true || skills[B].second == true) {
        skills[A].second = true, skills[B].second = true;
    }

    if (S[A] < S[B]) {
        G[A] = B;
        S[B] += S[A];
    } else {
        G[B] = A;
        S[A] += S[B];
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int i, n, m, q, skill;
    string name;
    cin >> n >> m >> q;

    for (i = 0; i < n; i++) {
        cin >> name >> skill;
        dict[name] = i;
        G[i] = i;
        S[i] = 1;
        skills[i] = make_pair(skill, false);
    }

    //cout << "\n\n\n";
    //for (auto &it : dict)
        //cout << it.first << " " << it.second << "\n";
    //cout << "\n\n\n";

    string p1, p2;
    for (i = 0; i < m; i++) {
        cin >> p1 >> p2;
        Union(dict[p1], dict[p2]);
    }

    int id, idParent;
    bool status;
    for (i = 0; i < q; i++) {
        cin >> name;
        id = dict[name];
        idParent = Find(id);

        //cout << "id: "<<id<<" parent: "<<idParent<<"\n";

        if (S[idParent]<2 || skills[id].first>=5)
            status = true;
        else if (!skills[idParent].second && !skills[id].second)
            status = true;
        else
            status = false;
        cout << (status ? "S\n" : "N\n");
    }

    return 0;
}
