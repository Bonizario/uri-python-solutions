#include <stdio.h>
#include <string.h>

int main(void)
{
    char clima_casa[6], clima_trabalho[6];
    int n, estoque[2] = {0, 0}, guarda_chuvas[2] = {0, 0};

    scanf("%d", &n);

    while (n--)
    {
        scanf("%s %s", clima_casa, clima_trabalho);

        if (strcmp(clima_casa, "chuva") == 0)
        {
            if (guarda_chuvas[0] == 0)
            {
                estoque[0]++;
            }
            else
            {
                guarda_chuvas[0]--;
            }
            guarda_chuvas[1]++;
        }
        if (strcmp(clima_trabalho, "chuva") == 0)
        {
            if (guarda_chuvas[1] == 0)
            {
                estoque[1]++;
            }
            else
            {
                guarda_chuvas[1]--;
            }
            guarda_chuvas[0]++;
        }
    }

    printf("%d %d\n", estoque[0], estoque[1]);

    return 0;
}
