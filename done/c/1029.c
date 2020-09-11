#include <stdio.h>

int chamadas;
int fib(int n);

int main(void)
{
    int f, n, t;
    scanf("%d", &t);

    while (t--)
    {
        chamadas = 0;
        scanf("%d", &n);
        f = fib(n);
        printf("fib(%d) = %d calls = %d\n", n, chamadas - 1, f);
    }

    return 0;
}

int fib(int n)
{
    chamadas++;
    return (n <= 1 ? n : fib(n - 1) + fib(n - 2));
}
