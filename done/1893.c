#include <stdio.h>

int main(void)
{
    int a, b;
    scanf("%d%d", &a, &b);

    if (b >= 0 && b <= 2)
    {
        printf("nova\n");
    }
    else if (b >= 97 && b <= 100)
    {
        printf("cheia\n");
    }

    if (b <= 96 && b >= 3)
    {
        if (a <= b)
        {
            printf("crescente\n");
        }
        else
        {
            printf("minguante\n");
        }
    }

    return 0;
}
