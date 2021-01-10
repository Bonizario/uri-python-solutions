#include <stdio.h>

int somas[450];

int busca(int n)
{
    int i;
    for (i = 0; i < 450; i++)
    {
        if (somas[i] == n)
        {
            return n;
        }
        else if (somas[i] > n)
        {
            return somas[i - 1];
        }
    }
}

int main(void)
{
    int i, n, fink;

    for (i = 0; i < 450; i++)
    {
        somas[i] = (i + i * i) / 2;
    }

    while (1)
    {
        scanf("%d", &n);
        if (n == 0)
        {
            break;
        }

        fink = busca(n);

        if (fink == n)
        {
            printf("%d 0\n", fink);
        }
        else
        {
            printf("%d %d\n", fink, n - fink);
        }
    }

    return 0;
}
