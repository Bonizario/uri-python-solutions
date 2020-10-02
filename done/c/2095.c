#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b)
{
    const int *pa = (const int *)a;
    const int *pb = (const int *)b;
    if (*pa <  *pb) return -1;
    if (*pa == *pb) return 0;
    if (*pa >  *pb) return 1;
}

int calculaVitorias(int S, int v1[], int v2[])
{
    int i = 0, j = 0, vitorias = 0;

    while (1)
    {
        while (i < S && v2[i] <= v1[j]) i++;
        if (i == S) return vitorias;
        vitorias++, i++, j++;
    }
}

int main(void)
{
    int i, j, S, v1[100000], v2[100000];
    scanf("%d", &S);

    for (i = 0; i < S; i++) scanf("%d", &v1[i]);
    for (i = 0; i < S; i++) scanf("%d", &v2[i]);

    qsort(v1, S, sizeof(int), cmp);
    qsort(v2, S, sizeof(int), cmp);

    int vitorias = calculaVitorias(S, v1, v2);

    printf("%d\n", vitorias);

    return 0;
}
