#include <stdio.h>

int main(void)
{
    long int a, b, c, d;
    scanf("%ld %ld %ld %ld", &a, &b, &c, &d);
    long int diferenca = a * b - c * d;
    printf("DIFERENCA = %ld\n", diferenca);

    return 0;
}
