#include <stdio.h>
#include <string.h>

int main(void)
{
    int i, j, n, tamanho_chave, tamanho_palavra;
    unsigned char letra, chave[50], mensagem[100010], *m;

    gets(chave);
    tamanho_chave = strlen(chave);

    scanf("%d", &n);
    getchar();

    while (n--)
    {
        j = 0;
        gets(mensagem);
        m = strtok(mensagem, " ");

        while (1)
        {
            tamanho_palavra = strlen(m);
            if (m[0] != 'a' && m[0] != 'e' && m[0] != 'i' && m[0] != 'o' && m[0] != 'u')
            {
                for (i = 0; i < tamanho_palavra; i++)
                {
                    letra = chave[j++] + m[i] - 97;
                    putchar(letra <= 122 ? letra : letra - 26);
                    if (j == tamanho_chave) j = 0;
                }
            }
            else
            {
                printf("%s", m);
            }

            m = strtok(NULL, " ");

            if (m != NULL)
            {
                putchar(' ');
            }
            else
            {
                putchar('\n');
                break;
            }
        }
    }

    return 0;
}
