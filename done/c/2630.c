#include <stdio.h>
#include <string.h>

int main(void)
{
    int caso = 1, t, r, g, b, cinza;
    char operacao[10];

    scanf("%d", &t);

    while (t--)
    {
        scanf("%s", operacao);
        scanf("%d %d %d", &r, &g, &b);

        if (strcmp(operacao, "min") == 0)
        {
            cinza = (r < g ? (r < b ? r : b) : (g < b ? g : b));
        }
        else if (strcmp(operacao, "max") == 0)
        {
            cinza = (r > g ? (r > b ? r : b) : (g > b ? g : b));
        }
        else if (strcmp(operacao, "mean") == 0)
        {
            cinza = (r + g + b) / 3.0;
        }
        else
        {
            cinza = (0.3 * r + 0.59 * g + 0.11 * b);
        }

        printf("Caso #%d: %d\n", caso++, cinza);
    }

    return 0;
}
