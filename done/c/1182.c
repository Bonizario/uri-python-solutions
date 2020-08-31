#include <stdio.h>

int main(void)
{
    char operacao;
    int i, j, coluna;
    double soma = 0, auxiliar;

    scanf("%d %c", &coluna, &operacao);

    for (i = 0; i < 12; i++)
    {
        for (j = 0; j < 12; j++)
        {
            scanf("%lf", &auxiliar);

            if (j == coluna)
            {
                soma += auxiliar;
            }
        }
    }

    printf("%.1lf\n", (operacao == 'S' ? soma : soma / 12.0));

    return 0;
}
