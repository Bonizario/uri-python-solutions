#include <iostream>
#define MAXN 10

using namespace std;

int isMagicSquare(int matrix[][MAXN], int N) {
    // return may be adapted to different problems
    int i, j;

    int primaryDiagonal = 0, secondaryDiagonal = 0;
    for (i = 0; i < N; i++) {
        primaryDiagonal += matrix[i][i];
        secondaryDiagonal += matrix[i][N-i-1];
    }

    if (primaryDiagonal != secondaryDiagonal)
        return -1;

    int rowSum, colSum;
    for (i = 0; i < N; i++) {
        rowSum = 0;
        colSum = 0;
        for (j = 0; j < N; j++) {
            rowSum += matrix[i][j];
            colSum += matrix[j][i];
        }

        if (rowSum != primaryDiagonal)
            return -1;
        if (colSum != primaryDiagonal)
            return -1;
    }

    return colSum;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int i, j, N, square[MAXN][MAXN];
    cin >> N;

    for (i = 0; i < N; i++)
        for (j = 0; j < N; j++)
            cin >> square[i][j];

    cout << isMagicSquare(square, N) << "\n";

    return 0;
}
