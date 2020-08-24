#include <stdio.h>

int main(void)
{
    int L, C, tipo1, tipo2;
    scanf("%d %d", &L, &C);
    tipo1 = 2 * L * C - L - C + 1;
    tipo2 = 2 * (L + C) - 4;

    printf("%d\n%d\n", tipo1, tipo2);

    return 0;
}
