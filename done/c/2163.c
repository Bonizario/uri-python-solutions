#include <stdio.h>

int main(void)
{
    short i, j, n, m, t[1000][1000];

    scanf("%hd %hd", &n, &m);

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            scanf("%hd", &t[i][j]);
        }
    }

    n -= 1, m -= 1;
    for (i = 1; i < n; i++)
    {
        for (j = 1; j < m; j++)
        {
            if (t[i][j]     == 42 && t[i][j-1] == 7 && t[i][j+1]   == 7 &&
                t[i-1][j-1] == 7  && t[i-1][j] == 7 && t[i-1][j+1] == 7 &&
                t[i+1][j-1] == 7  && t[i+1][j] == 7 && t[i+1][j+1] == 7)
            {
                printf("%hd %hd\n", i + 1, j + 1);
                return 0;
            }
        }
    }

    puts("0 0");

    return 0;
}
