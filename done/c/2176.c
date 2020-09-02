#include <stdio.h>
#include <string.h>

int main(void)
{
    size_t tamanho;
    int i, contador;
    char bits[101];

    scanf("%s", bits);

    for (i = 0, tamanho = strlen(bits); i < tamanho; i++)
    {
        if (bits[i] == '1')
        {
            contador++;
        }
    }

    printf("%s%c\n", bits, (contador & 1 ? '1' : '0'));

    return 0;
}
