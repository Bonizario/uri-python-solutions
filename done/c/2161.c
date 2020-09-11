#include <stdio.h>

double calculaRaiz(double n)
{
    if (n == 0)
    {
        return 0;
    }
    return 1 / (2 + calculaRaiz(n - 1));
}

int main(void)
{
    int n;

    scanf("%d", &n);

    printf("%.10f\n", 1 + calculaRaiz(n));

    return 0;
}
