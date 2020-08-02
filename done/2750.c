#include <stdio.h>

int main()
{
    printf("---------------------------------------\n");
    printf("|  decimal  |  octal  |  Hexadecimal  |\n");
    printf("---------------------------------------\n");

    int i;
    for (i = 0; i <= 15; i++)
    {
        printf("|     %*d    |   %*o    |      %*X       |\n", 2, i, 2, i, 2, i);
    }
    printf("---------------------------------------\n");

    return 0;
}
