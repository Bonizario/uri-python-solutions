#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void imprime_binario(int decimal, int *binario);

int main(void)
{
    char num[33], base[33];
    int i, n, decimal, binario[33];

    scanf("%d", &n);

    for (i = 1; i <= n; i++)
    {
        scanf("%s %s", num, base);
        printf("Case %d:\n", i);

        if (strcmp(base, "bin") == 0)
        {
            decimal = strtol(num, NULL, 2);
            printf("%d dec\n", decimal);
            printf("%x hex\n\n", decimal);
        }
        else if (strcmp(base, "dec") == 0)
        {
            decimal = atoi(num);
            printf("%x hex\n", decimal);
            imprime_binario(decimal, binario);
        }
        else
        {
            decimal = strtol(num, NULL, 16);
            printf("%d dec\n", decimal);
            imprime_binario(decimal, binario);
        }
    }

    return 0;
}

void imprime_binario(int decimal, int *binario)
{
    int i;
    for (i = 0; decimal > 0; i++)
    {
        binario[i] = decimal % 2;
        decimal /= 2;
    }

    for(i -= 1; i >= 0; i--)
    {
        printf("%d", binario[i]);
    }
    puts(" bin\n");
}
