#include <stdio.h>

void traces();

int main()
{
    traces();
    printf("|x = 35                               |\n");
    printf("|                                     |\n");
    printf("|               x = 35                |\n");
    printf("|                                     |\n");
    printf("|                               x = 35|\n");
    traces();

    return 0;
}

void traces()
{
    int i;
    for (i = 0; i < 39; i++)
    {
        putchar('-');
    }
    putchar('\n');
    return;
}
