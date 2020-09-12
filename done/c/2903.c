#include <stdio.h>
#include <math.h>
#define EPS 0.000000001

int main(void)
{
    int i;
    double r, resto, total = 360.0;

    scanf("%lf", &r);

    while (1)
    {
        resto = fmod(total, r);

        if (resto < EPS)
        {
            break;
        }

        total = r, r = resto;
    }

    printf("%.0f\n", 360.0 / r);

    return 0;
}
