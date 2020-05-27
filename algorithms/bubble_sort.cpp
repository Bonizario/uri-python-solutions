/*
    bubble sort uses 2 nested for loops, which implies an
    O(n^2) time complexity in the worst case scenario.
    The array in reverse order takes:
        1 + 2 + ... + (n - 1) = n(n - 1)/2 = O(n^2)
    inversions.

    There are also merge sort O(nlogn) and counting sort O(n).

    It is almost never a good idea to implement a sorting algorithm,
    instead, use the sort() function from the STL (C++) or
    the qsort() function (C).
*/

void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

void bubbleSort(int arr[], int N) {
    int i, j;
    for (i = 0; i < N-1; i++)
        for (j = 0; j < N-i-1; j++)
            if (arr[j] > arr[j+1])
                swap(&arr[j], &arr[j+1]);
}
