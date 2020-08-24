#include <stdio.h>

int main(void)
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    if (a > b && b <= c)
    {
        printf(":)\n");
    }
    else if (a < b && c <= b)
    {
        printf(":(\n");
    }
    else if (a < b && b < c)
    {
        if (c - b < b - a)
        {
            printf(":(\n");
        }
        else
        {
            printf(":)\n");
        }
    }
    else if (a > b && b > c)
    {
        if (b - c < a - b)
        {
            printf(":)\n");
        }
        else
        {
            printf(":(\n");
        }
    }
    else if (a == b)
    {
        if (c > b)
        {
            printf(":)\n");
        }
        else
        {
            printf(":(\n");
        }
    }

    return 0;
}
