#include <stdio.h>

typedef long long unsigned int llu;

int main(void)
{
    int i, n, t;
    scanf("%d", &t);

    llu fib[61];
    fib[0] = 0, fib[1] = 1;
    for (i = 2; i <= 60; i++)
    {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    while (t--)
    {
        scanf("%d", &n);
        printf("Fib(%d) = %llu\n", n, fib[n]);
    }

    return 0;
}
