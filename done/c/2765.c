#include <stdio.h>
#include <string.h>

int main(void)
{
    char frase[500], *c;

    while (gets(frase) != NULL)
    {
        c = strtok(frase, ",");
        puts(c);
        c = strtok(NULL, ",");
        puts(c);
    }

    return 0;
}
