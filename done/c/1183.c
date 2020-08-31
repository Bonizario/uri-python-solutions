#include <stdio.h>

int main(void)
{
    int i, j;
    char operacao;
    double soma = 0, auxiliar;

    scanf("%c", &operacao);

    for (i = 0; i < 12; i++)
    {
        for (j = 0; j < 12; j++)
        {
            scanf("%lf", &auxiliar);

            if (j > i)
            {
                soma += auxiliar;
            }
        }
    }

    printf("%.1f\n", (operacao == 'S' ? soma : soma / 66.0));

    return 0;
}
