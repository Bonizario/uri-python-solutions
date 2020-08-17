#include <stdio.h>

int main(void)
{
    int m, a, b;
    scanf("%d%d%d", &m, &a, &b);
    int c = m - a - b;

    printf("%d\n", (a > b ? (a > c ? a : c) : (b > c ? b : c)));

    return 0;
}
