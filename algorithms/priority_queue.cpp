/*
    std::priority_queue is a container adaptor that provides
    constant time lookup of the largest OR smallest element.
    By default, std::vector is the container used inside.
    Acessing the top element is O(1), insertion/extraction is O(logn).
    It is implemented using std::make_heap, std::push_heap and std::pop_heap.
*/

#include <functional>  // std::greater<int>
#include <queue>
#include <vector>

using namespace std;

int main() {
    // max-heap by default with vector+less (top element is the biggest)
    priority_queue<int> pq;
    for (int elm : {1, 8, 5, 6, 3, 4, 0, 9, 7, 2}) {
        pq.push(elm);
    }

    // min-heap with vector+greater, (top element is the smallest)
    priority_queue<int, vector<int>, greater<int>> pq2;
    for (int elm : {1, 8, 5, 6, 3, 4, 0, 9, 7, 2}) {
        pq2.push(elm);
    }

    // custom compare function
    auto cmp = [](int left, int right) { return (left) < (right); };
    priority_queue<int, vector<int>, decltype(cmp)> pq3;
    for (int elm : {1, 8, 5, 6, 3, 4, 0, 9, 7, 2}) {
        pq3.push(elm);
    }

    // pq of pairs in ascending order (first item in pair)
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;

    return 0;
}

// custom cmp function and custom struct (2065-URI)
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
