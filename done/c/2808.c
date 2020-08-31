#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int i1, i2;;
    char j1, j2;

    scanf("%c%d %c%d", &j1, &i1, &j2, &i2);

    j1 = (int) j1 - 96, j2 = (int) j2 - 96;

    if (abs(j1 - j2) + abs(i1 - i2) == 3)
    {
        printf("VALIDO\n");
    }
    else
    {
        printf("INVALIDO\n");
    }

    return 0;
}

/*
// Dynamic programming Floyd Warshall algorithm to compute
// the minimum steps required to reach any target by a Knight.

#include <stdio.h>

const int POSITIVE_INFINITY = 9999;

int main(void)
{
    int i, j, k;

    int dp[64][64];
    for (i = 0; i < 64; i++)
    {
        for (j = 0; j < 64; j++)
        {
            dp[i][j] = POSITIVE_INFINITY;
        }
    }

    for (i = 0; i < 8; i++)
    {
        for (j = 0; j < 8; j++)
        {
            int atual = 8 * i + j;
            if (i > 1)
            {
                if (j > 0)
                {
                    dp[atual][8 * (i - 2) + j - 1] = 1;
                }
                if (j < 7)
                {
                    dp[atual][8 * (i - 2) + j + 1] = 1;
                }
            }
            if (i < 6)
            {
                if (j > 0)
                {
                    dp[atual][8 * (i + 2) + j - 1] = 1;
                }
                if (j < 7)
                {
                    dp[atual][8 * (i + 2) + j + 1] = 1;
                }
            }
            if (j > 1)
            {
                if (i > 0)
                {
                    dp[atual][8 * (i - 1) + j - 2] = 1;
                }
                if (i < 7)
                {
                    dp[atual][8 * (i + 1) + j - 2] = 1;
                }
            }
            if (j < 6)
            {
                if (i > 0)
                {
                    dp[atual][8 * (i - 1) + j + 2] = 1;
                }
                if (i < 7)
                {
                    dp[atual][8 * (i + 1) + j + 2] = 1;
                }
            }
        }
    }

    for (k = 0; k < 64; k++)
    {
        for (i = 0; i < 64; i++)
        {
            for (j = 0; j < 64; j++)
            {
                if (dp[i][j] > dp[i][k] + dp[k][j])
                {
                    dp[i][j] = dp[i][k] + dp[k][j];
                }
            }
        }
    }

    int i1, i2;
    char j1, j2;

    scanf("%c%d %c%d", &j1, &i1, &j2, &i2);

    i1 -= 1, i2 -= 1;
    j1 = (int) j1 - 97, j2 = (int) j2 - 97;

    printf("\nSteps required: %d\n\n", dp[8 * i1 + j1][8 * i2 + j2]);

    return 0;
}
*/
