#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Func {
    unsigned total, time_per_item, id;
};

struct Compare {
    bool operator()(const Func &a, const Func &b) {
        if (a.total != b.total) return a.total > b.total;
        else return a.id > b.id;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    priority_queue<Func, vector<Func>, Compare> pq;
    Func f;

    unsigned i, n, m, aux, total_time = 0;
    cin >> n >> m;

    for (i = 1; i <= n; i++) {
        cin >> f.time_per_item;
        f.total = 0;
        f.id = i;
        pq.push(f);
    }

    for (i = 1; i <= m; i++) {
        cin >> aux;
        f = pq.top();
        pq.pop();
        f.total += f.time_per_item * aux;
        //cout << f.id << " " << f.time_per_item << " " << f.total << "\n";
        pq.push(f);
    }

    for (i = 1; i <= n; i++) {
        f = pq.top();
        pq.pop();
        if (total_time < f.total)
            total_time = f.total;
    }
    cout << total_time << "\n";

    return 0;
}
