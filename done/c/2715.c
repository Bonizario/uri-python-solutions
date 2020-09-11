#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int i, n, d, *dificuldades = (int *) malloc(1e6 * sizeof(int));
    long long antes, depois, gugu, rangel;

    while (scanf("%d", &n) != EOF)
    {
        gugu = rangel = 0;
        for (i = 0; i < n; i++)
        {
            scanf("%d", &dificuldades[i]), rangel += dificuldades[i];
        }

        if (n == 1)
        {
            printf("%d\n", dificuldades[0]);
            continue;
        }

        for (i = 0; i < n; i++)
        {
            d = dificuldades[i];
            antes = llabs(rangel - gugu);
            gugu += d, rangel -= d;
            depois = llabs(rangel - gugu);

            if (antes < depois)
            {
                printf("%lld\n", antes);
                break;
            }
        }
    }

    free(dificuldades);

    return 0;
}
