#include <stdio.h>
#include <string.h>

int main(void)
{
    size_t tamanho;
    char s[11];
    int ok, calc;

    while (scanf("%s", s) != EOF)
    {
        ok = 0;
        tamanho = strlen(s);

        switch (tamanho)
        {
            case 1:
                printf("%d\n", s[0] - 64);
                break;
            case 2:
                printf("%d\n", (s[0] - 64) * 26 + s[1] - 64);
                break;
            case 3:
                calc = (s[0] - 64) * 676 + (s[1] - 64) * 26 + (s[2] - 64);
                if (calc <= 16384)
                {
                    printf("%d\n", calc);
                    break;
                }
            default:
                printf("Essa coluna nao existe Tobias!\n");
        }
    }

    return 0;
}
