#include <stdio.h>

int main(void)
{
    int i, n, a = 0, b = 1, agora = 0;
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        if (i == 0)
        {
            putchar('0');
        }
        else if (i == 1)
        {
            printf(" 1");
        }
        else
        {
            agora = a + b;
            printf(" %d", agora);
            a = b, b = agora;
        }
    }
    putchar('\n');

    return 0;
}
