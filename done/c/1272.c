#include <stdio.h>
#include <string.h>

int main(void)
{
    int n;
    char texto[55], mensagem[55], *c;

    scanf("%d", &n);
    getchar();

    while (n--)
    {
        gets(texto);
        c = strtok(texto, " ");

        while (c != NULL)
        {
            putchar(c[0]);
            c = strtok(NULL, " ");
        }
        putchar('\n');
    }

    return 0;
}
