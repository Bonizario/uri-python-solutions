#include <stdio.h>

int main(void)
{
    long long unsigned a, b;
    scanf("%llu %llu", &a, &b);
    printf("%llu\n", (a + b) * (b - a + 1) / 2);

    return 0;
}
