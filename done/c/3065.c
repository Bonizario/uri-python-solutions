#include <stdio.h>

int main(void)
{
    int m, resultado, numero, teste = 1;

    while (scanf("%d", &m) && m)
    {
        resultado = 0;

        while (m--)
        {
            scanf("%d", &numero);
            resultado += numero;
        }

        printf("Teste %d\n%d\n\n", teste++, resultado);
    }

    return 0;
}
