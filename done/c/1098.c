#include <stdio.h>

int main(void)
{
    double i, j;
    for (i = 0; i <= 2; i += 0.2)
    {
        for (j = i + 1; j <= i + 3; j++)
        {
            printf("I=%G J=%G\n", i, j);
        }
    }

    return 0;
}
