#include <stdio.h>
#include <string.h>

int main(void)
{
    int i, j, n, meio, fim;
    char frase[102], decifrada[102];

    scanf("%d", &n);
    getchar();

    while (n--)
    {
        gets(frase);

        j = 0, fim = strlen(frase) - 1, meio = (int) fim / 2;

        for (i = meio; i >= 0; i--)
        {
            decifrada[j++] = frase[i];
        }

        for (i = fim; i > meio; i--)
        {
            decifrada[j++] = frase[i];
        }

        decifrada[j] = '\0';
        printf("%s\n", decifrada);
    }

    return 0;
}
