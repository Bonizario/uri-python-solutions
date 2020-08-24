#include <stdio.h>

int main(void)
{
    int n, pecas;
    scanf("%d", &n);
    pecas = 0.5 * n * n + 1.5 * n + 1;
    printf("%d\n", pecas);

    return 0;
}
