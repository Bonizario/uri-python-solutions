#include <stdio.h>

int main(void)
{
    int i, n, porta, ganhou = 0;

    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &porta);
        ganhou += (porta != 1 ? 1 : 0);
    }
    printf("%d\n", ganhou);

    return 0;
}
