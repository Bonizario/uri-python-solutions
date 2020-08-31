#include <stdio.h>

int main(void)
{
    double x;
    scanf("%lf", &x);

    int i;
    for (i = 0; i < 100; i++)
    {
        printf("N[%d] = %.4lf\n", i, x);
        x /= 2.0;
    }

    return 0;
}
