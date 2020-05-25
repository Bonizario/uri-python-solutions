/*
    bubble sort uses 2 nested for loops, which implies an
    O(n^2) time complexity in the worst case scenario.
    The array in reverse order takes:
        1 + 2 + ... + (n - 1) = n(n - 1)/2 = O(n^2)
    inversions.

    There are also merge sort O(nlogn) and counting sort O(n).

    It is almost never a good idea to implement a sorting algorithm,
    instead, use the sort() function from the STL.
*/

int bubbleSort(int arr[], int size) {
    int i, j, aux;
    for (i = 0; i < size; i++) {
        for (j = 0; j < size-1; j++) {
            aux = arr[j];
            if (aux > arr[j+1]) {
                arr[j] = arr[j+1];
                arr[j+1] = aux;
            }
        }
    }
}
