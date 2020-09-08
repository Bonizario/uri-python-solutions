#include <stdio.h>
#include <string.h>

int main(void)
{
    int n, tamanho;
    char palavra[25];

    scanf("%d", &n);

    while (n--)
    {
        scanf("%s", palavra);
        tamanho = strlen(palavra);

        if (tamanho == 3)
        {
            if ((palavra[0] == 'O' && palavra[1] == 'B') ||
                (palavra[0] == 'U' && palavra[1] == 'R'))
            {
                palavra[2] = 'I';
            }
        }

        printf("%s%c", palavra, (n ? ' ' : '\n'));
    }

    return 0;
}

/* SOLUTION WITH POINTERS
#include <stdio.h>
#include <string.h>

int main(void)
{
    int primeira = 1, n;
    char palavras[200005], *c;

    scanf("%d", &n);
    getchar();

    gets(palavras);

    c = strtok(palavras, " ");

    while (c != NULL)
    {
        if (strlen(c) == 3 &&
           ((c[0] == 'O' && c[1] == 'B') ||
            (c[0] == 'U' && c[1] == 'R')))
        {
            c[2] = 'I';
        }
        if (primeira)
        {
            printf("%s", c);
            primeira = 0;
        }
        else
        {
            printf(" %s", c);
        }
        c = strtok(NULL, " ");
    }

    putchar('\n');

    return 0;
}
*/
