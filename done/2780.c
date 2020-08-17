#include <stdio.h>

int main(void)
{
    int D;
    scanf("%d", &D);

    printf("%d\n", (D <= 800 ? 1 : D <= 1400 ? 2 : 3));

    return 0;
}
