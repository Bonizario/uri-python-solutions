#include <stdio.h>

int main(void)
{
    int i, n, fib[40];
    fib[0] = 1, fib[1] = 1;

    for (i = 2; i < 40; i++)
    {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    scanf("%d", &n);

    for (i = n - 1; i > 0; i--)
    {
        printf("%d ", fib[i]);
    }
    printf("%d\n", fib[0]);

    return 0;
}
