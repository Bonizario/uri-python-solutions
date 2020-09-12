#include <stdio.h>
#include <string.h>

int main(void)
{
    char *c, expressao[20000];
    int i, j, m, resultado, teste = 1, numeros[20000], operacoes[2000];

    while (scanf("%d", &m) && m)
    {
        scanf("%s", expressao);

        if (m == 1)
        {
            printf("Teste %d\n%s\n\n", teste++, expressao);
            continue;
        }

        i = j = 0;
        while (expressao[i])
        {
            if (expressao[i] == '+')
            {
                operacoes[j++] = 1;
            }
            else if (expressao[i] == '-')
            {
                operacoes[j++] = 0;
            }
            i++;
        }

        c = strtok(expressao, "+-");
        numeros[0] = atoi(c);

        i = 1;
        while (1)
        {
            c = strtok(NULL, "+-");
            if (c != NULL)
            {
                numeros[i++] = atoi(c);
            }
            else
            {
                break;
            }
        }

        resultado = numeros[0];
        for (i = 0, m -= 1; i < m; i++)
        {
            if (operacoes[i])
            {
                resultado += numeros[i + 1];
            }
            else
            {
                resultado -= numeros[i + 1];
            }
        }

        printf("Teste %d\n%d\n\n", teste++, resultado);
    }

    return 0;
}
