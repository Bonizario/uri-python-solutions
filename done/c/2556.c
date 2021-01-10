#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

int main(void)
{
    int i, n, meio, arr[1000];

    while (scanf("%d", &n) != EOF)
    {
        for (i = 0; i < n; i++)
        {
            scanf("%d", &arr[i]);
        }

        qsort(arr, n, sizeof(int), cmp);

        meio = n / 2;

        printf("%d %d\n", meio, arr[meio] - arr[meio - 1]);
    }

    return 0;
}
