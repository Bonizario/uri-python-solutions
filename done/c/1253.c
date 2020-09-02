#include <stdio.h>
#include <string.h>

int main(void)
{
    size_t tamanho;
    int i, n, ascii, deslocamento;
    char original[51], decodificado[51];

    scanf("%d", &n);

    while (n--)
    {
        scanf("%s", original);
        scanf("%d", &deslocamento);

        for (i = 0, tamanho = strlen(original); i < tamanho; i++)
        {
            ascii = (int) original[i] - deslocamento;

            decodificado[i] = (ascii < 65 ? 26 + ascii : ascii);
        }
        decodificado[i] = '\0';

        printf("%s\n", decodificado);
    }

    return 0;
}
