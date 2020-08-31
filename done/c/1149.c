#include <stdio.h>

int main(void)
{
    int a, n;
    scanf("%d", &a);

    do
    {
        scanf("%d", &n);
    }
    while (n <= 0);

    printf("%d\n", (a + a + n - 1) * n / 2);

    return 0;
}
