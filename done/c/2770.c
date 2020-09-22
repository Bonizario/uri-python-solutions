#include <stdio.h>

int main(void)
{
    int x, y, m, xi, yi;

    while (scanf("%d %d %d", &x, &y, &m) != EOF)
    {
        while (m--)
        {
            scanf("%d %d", &xi, &yi);
            if (xi <= x && yi <= y || xi <= y && yi <= x)
                puts("Sim");
            else
                puts("Nao");
        }
    }

    return 0;
}
