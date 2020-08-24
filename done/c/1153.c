#include <stdio.h>

typedef long long unsigned int llu;
llu factorial(llu);

int main(void)
{
    llu n;
    scanf("%llu", &n);

    printf("%llu\n", factorial(n));

    return 0;
}

llu factorial(llu n)
{
    return (n <= 1 ? 1 : factorial(n - 1) * n);
}
