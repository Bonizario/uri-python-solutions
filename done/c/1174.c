#include <stdio.h>

int main(void)
{
    int i;
    double x;

    for (i = 0; i < 100; i++)
    {
        scanf("%lf", &x);

        if (x <= 10)
        {
            printf("A[%d] = %.1f\n", i, x);
        }
    }

    return 0;
}
