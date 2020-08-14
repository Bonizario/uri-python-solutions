#include <stdio.h>

int main()
{
    printf("---------------------------------------\n");
    printf("|  decimal  |  octal  |  Hexadecimal  |\n");
    printf("---------------------------------------\n");

    int i;
    for (i = 0; i <= 15; i++)
    {
        printf("|     %2d    |   %2o    |      %2X       |\n", i, i, i);
    }
    printf("---------------------------------------\n");

    return 0;
}
