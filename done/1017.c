#include <stdio.h>

int main(void)
{
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%.3lf\n", (double) a * b / 12);

    return 0;
}
