#include <stdio.h>
#include <string.h>

int main(void)
{
    char s[55];
    int i, j, q, n, t, tamanho, contador;

    scanf("%d", &t);

    while (t--)
    {
        scanf("%d", &q);
        contador = 0;

        for (i = 0; i < q; i++)
        {
            scanf("%s", s);
            tamanho = strlen(s);

            for (j = 0; j < tamanho; j++)
            {
                contador += (i + j + s[j] - 65);
            }
        }

        printf("%d\n", contador);
    }

    return 0;
}
