#include <stdio.h>

int main(void)
{
    int novo_calculo = 1;

    while (novo_calculo == 1)
    {
        int contador = 2;
        float x, media = 0;

        while (contador)
        {
            scanf("%f", &x);

            if (x >= 0 && x <= 10)
            {
                media += x, contador--;
            }
            else
            {
                printf("nota invalida\n");
            }
        }

        printf("media = %.2f\n", media / 2.0);

        do
        {
            printf("novo calculo (1-sim 2-nao)\n");
            scanf("%d", &novo_calculo);
        }
        while (novo_calculo != 1 && novo_calculo != 2);
    }

    return 0;
}
