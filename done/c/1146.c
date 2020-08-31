#include <stdio.h>

int main(void)
{
    int i, x;

    while (1)
    {
        scanf("%d", &x);

        if (!x)
        {
            break;
        }

        for (i = 1; i < x; i++)
        {
            printf("%d ", i);
        }
        printf("%d\n", i);
    }

    return 0;
}
