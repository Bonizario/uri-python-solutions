#include <stdio.h>

int main(void)
{
    int i;
    for (i = 0; i < 39; i++)
    {
        printf("-");
    }
    printf("\n");

    for (i = 0; i < 5; i++)
    {
        printf("|%*c|\n", 37, ' ');
    }

    for (i = 0; i < 39; i++)
    {
        printf("-");
    }
    printf("\n");

    return 0;
}
