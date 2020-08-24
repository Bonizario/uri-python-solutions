#include <stdio.h>

int main(void)
{
    float a, b, c;
    scanf("%f %f %f", &a, &b, &c);

    if (b >= a && b >= c)
    {
        a = a + b, b = a - b, a = a - b;
    }
    else if (c >= a && c >= b)
    {
        a = a + c, c = a - c, a = a - c;
    }
    if (c > b)
    {
        b = b + c, c = b - c, b = b - c;
    }

    if (a >= b + c)
    {
        printf("NAO FORMA TRIANGULO\n");
    }
    else
    {
        if (a * a == b * b + c * c)
        {
            printf("TRIANGULO RETANGULO\n");
        }
        if (a * a > b * b + c * c)
        {
            printf("TRIANGULO OBTUSANGULO\n");
        }
        if (a * a < b * b + c * c)
        {
            printf("TRIANGULO ACUTANGULO\n");
        }
        if (a == b && b == c)
        {
            printf("TRIANGULO EQUILATERO\n");
        }
        else if (a == b || b == c || a == c)
        {
            printf("TRIANGULO ISOSCELES\n");
        }
    }

    return 0;
}
