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
