#include <stdio.h>

int main(void)
{
    int i, n, min, max, altura;

    while (scanf("%d %d %d", &n, &min, &max) != EOF)
    {
        int total = 0;
        for (i = 0; i < n; i++)
        {
            scanf("%d", &altura);

            if (altura >= min && altura <= max)
            {
                total++;
            }
        }
        printf("%d\n", total);
    }


    return 0;
}
