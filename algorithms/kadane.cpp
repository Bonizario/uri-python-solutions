#include <algorithm> // max function

using namespace std;

int maxSubarraySum(int arr[], int size) { // vector<int> works aswell
    int i, max_sum = arr[0], current_sum = arr[0];
    for (i = 1; i < size; i++) {
        current_sum = max(arr[i], arr[i] + current_sum);
        max_sum = max(max_sum, current_sum);
    }

    return max_sum;
}
