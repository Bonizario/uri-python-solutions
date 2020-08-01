#include <stdio.h>

void traces();

int main()
{
    traces();
    printf("|  decimal  |  octal  |  Hexadecimal  |\n");
    traces();

    int i;
    for (i = 0; i <= 15; i++)
    {
        printf("|     %*d    |   %*o    |      %*X       |\n", 2, i, 2, i, 2, i);
    }
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
