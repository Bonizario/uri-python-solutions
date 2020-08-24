#include <stdio.h>

int main()
{
    int i;
    printf("---------------------------------------\n");
    for (i = 0; i < 5; i++)
    {
        printf("|%*c|\n", 37, ' ');
    }
    printf("---------------------------------------\n");

    return 0;
}
