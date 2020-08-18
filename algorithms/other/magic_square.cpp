#include <bits/stdc++.h>
using namespace std;

int isMagicSquare(const vector<vector<int>> &matrix, int n) {
    int rowSum, colSum, primaryDiagonal = 0, secondaryDiagonal = 0;

    for (int i = 0; i < n; i++) {
        primaryDiagonal += matrix[i][i];
        secondaryDiagonal += matrix[i][n-i-1];
    }

    if (primaryDiagonal != secondaryDiagonal)
        return -1;

    for (int i = 0; i < n; i++) {
        rowSum = 0, colSum = 0;

        for (int j = 0; j < n; j++) {
            rowSum += matrix[i][j];
            colSum += matrix[j][i];
        }

        if (rowSum != primaryDiagonal)
            return -1;
        if (colSum != primaryDiagonal)
            return -1;
    }

    return primaryDiagonal;
}
