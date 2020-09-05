#include <stdio.h>
#include <string.h>

int main(void)
{
    int i, n, t, ok;
    char placa[10];

    scanf("%d", &n);
    getchar();

    while (n--)
    {
        ok = 1;
        gets(placa);
        t = strlen(placa);

        if (t != 8 || placa[3] != '-')
        {
            ok = 0;
        }
        for (i = 0; i < t && ok; i++)
        {
            if (((i <= 2) && (placa[i] < 'A' || placa[i] > 'Z')) ||
                ((i >= 4) && (placa[i] < '0' || placa[i] > '9')))
            {
                ok = 0;
            }
        }
        if (!ok)
        {
            printf("FAILURE\n");
            continue;
        }
        switch(placa[t - 1])
        {
            case '1': printf("MONDAY\n");    break;
            case '2': printf("MONDAY\n");    break;
            case '3': printf("TUESDAY\n");   break;
            case '4': printf("TUESDAY\n");   break;
            case '5': printf("WEDNESDAY\n"); break;
            case '6': printf("WEDNESDAY\n"); break;
            case '7': printf("THURSDAY\n");  break;
            case '8': printf("THURSDAY\n");  break;
            case '9': printf("FRIDAY\n");    break;
            case '0': printf("FRIDAY\n");    break;
        }
    }

    return 0;
}
