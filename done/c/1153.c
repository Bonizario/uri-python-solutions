#include <stdio.h>

int factorial(int n)
{
    return (n <= 1 ? 1 : factorial(n - 1) * n);
}

int main(void)
{
    int n;
    scanf("%d", &n);

    printf("%d\n", factorial(n));

    return 0;
}
