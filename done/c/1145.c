#include <stdio.h>

int main(void)
{
    int i, x, y;
    scanf("%d %d", &x, &y);
    int contador = 0;

    for (i = 1; i <= y; i++)
    {
        contador++;
        printf("%d", i);

        if (contador == x)
        {
            putchar('\n'), contador = 0;
        }
        else
        {
            putchar(' ');
        }
    }

    return 0;
}
