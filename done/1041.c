#include <stdio.h>

int main(void)
{
    float x, y;
    scanf("%f %f", &x, &y);

    if (!x && !y)
    {
        printf("Origem\n");
    }
    else if (!x && y)
    {
        printf("Eixo Y\n");
    }
    else if (x && !y)
    {
        printf("Eixo X\n");
    }
    else
    {
        if (x > 0)
        {
            if (y > 0)
            {
                printf("Q1\n");
            }
            else
            {
                printf("Q4\n");
            }
        }
        else
        {
            if (y > 0)
            {
                printf("Q2\n");
            }
            else
            {
                printf("Q3\n");
            }
        }
    }

    return 0;
}
