#include <stdio.h>

int forma_triangulo(int a, int b, int c)
{
    return (a < b + c && b < a + c && c < a + b);
}

int main(void)
{
    int a, b, c, d;

    scanf("%d %d %d %d", &a, &b, &c, &d);

    if (forma_triangulo(a, b, c) ||
        forma_triangulo(a, b, d) ||
        forma_triangulo(a, c, d) ||
        forma_triangulo(b, c, d))
    {
        puts("S");
    }
    else
    {
        puts("N");
    }

    return 0;
}
