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
