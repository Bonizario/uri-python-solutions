/*
    Array with N elements: N -> N/2 -> N/4 -> ... -> 1 -> 0
    log2(N) describes this behavior
    Time complexity = O(log2(N)) = O(log(N))
*/

// WRONG! WRONG! WRONG! WRONG! WRONG!
// M = (L + R) / 2; (L + R) can cause an overflow, use L + (R - L)

int binarySearch(int arr[], int target, int N) {
    int mid, L = 0, R = N - 1;

    while (L <= R) {
        mid = L + (R - L) / 2;

        if (arr[mid] == target)
            return mid;
        if (arr[mid] < target)
            L = mid + 1;
        else
            R = mid - 1;
    }

    return -1;
}

// Is x an square number?
// Solution: binary search i in [0, x], checking if i*i == x
int isSquareNumber(int arr[], int target, int N) {
    int mid, square;
    int L = 0, R = N - 1;

    while (L <= R) {
        mid = L + (R - L) / 2;
        square = arr[mid] * arr[mid];

        if (square == target)
            return mid;
        if (square < target)
            L = mid + 1;
        else
            R = mid - 1;
    }

    return -1;
}

// Lower bound, find first value >= x.
// Solution: create ans; if arr[mid] >= x, ans = arr[mid], keep searching ans.
int lowerBound(int arr[], int x, int N) {
    int mid;
    int L = 0, R = N - 1;
    int ans = -1;
    // ans could be -infinity, NULL pointer...

    while (L <= R) {
        mid = L + (R - L) / 2;

        if (arr[mid] >= x) {
            ans = mid; // ans could be arr[mid]
            R = mid - 1; // if there is a better option, is on the left
        } else {
            L = mid + 1;
        }
    }

    return ans;
}
// You should think about in which half the better option is!
// In some problems, the order of the above if/else is reversed
// We should think that 1 condition is satisfied or not for every element
// E.g. [2,3,5,6,8,10,12], condition: x>=4
// Then,[F,F,T,T,T,T,T]


// Rotated array, someone rotated (shifted) a sorted array.
// Find the smallest element. [2,3,6,7,9,15,19] -> [6,7,9,15,19,2,3]
// We should compare the middle to the first and last
#include <vector>

int findMinRotatedArray(std::vector<int> nums) {
    int N = nums.size(), mid;
    int L = 0, R = N - 1;
    int ans = -1;

    while (L <= R) {
        mid = L + (R - L) / 2;

        if (nums[mid] <= nums[N-1]) {
            ans = nums[mid]; // could be ans = mid
            R = mid - 1;
        } else {
            L = mid + 1;
        }
    }

    return ans;
}


// Find peak. The array increases and then decreases.
// Find the maximum element. [2,3,4,6,9,12,11,8,6,4,1]
// To Do
