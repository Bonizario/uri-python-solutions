#include <stdio.h>

int main(void)
{
    int i, n;

    for (i = 0; i < 10; i++)
    {
        scanf("%d", &n);
        printf("X[%d] = %d\n", i, (n <= 0 ? 1 : n));
    }

    return 0;
}
