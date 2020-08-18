#include <iostream>
#include <algorithm>
#include <functional>  // greater<int>()
#include <vector>

using namespace std;

bool comp(string a, string b) {
    if (a.size() != b.size()) return a.size() < b.size();
    return a < b;
}

int main() {
    // ordinary array
    int arr[] = {1, 5, 8, 9, 6, 7, 3, 4, 2, 0};

    sort(arr, arr + 10); // ascending order

    sort(arr, arr +  10, greater<int>()); // descending order

    // greater<>() can also be used with merge, lower_bound, upper_bound,
    // if the container is sorted in descending order

    // vector
    vector < int > V = {1, 5, 8, 9, 6, 7, 3, 4, 2, 0};

    sort(V.begin(), V.end()); // ascending order

    sort(V.rbegin(), V.rend()); // descending order

    // string
    string s = "mOnKey";
    sort(s.begin(), s.end(), comp); // ascending order: KOemny

    sort(s.rbegin(), s.rend()); // descending order: ynmeOK

    // vector of strings with custom comparing function -> size, ascending
    vector < string > S = {"mOnkey", "Rat", "dog", "manana"};

    sort(S.begin(), S.end(), comp); // Rat dog mOnkey manana

    // for (int i = 0; i < S.size(); i++) {
    //     cout << S[i] << " ";
    // }

    return 0;
}
