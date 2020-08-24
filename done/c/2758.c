#include <stdio.h>

int main(void)
{
    float a, b;
    double c, d;
    scanf("%f %f %lf %lf", &a, &b, &c, &d);
    printf("A = %f, B = %f\n", a, b);
    printf("C = %f, D = %f\n", c, d);
    printf("A = %.1f, B = %.1f\n", a, b);
    printf("C = %.1f, D = %.1f\n", c, d);
    printf("A = %.2f, B = %.2f\n", a, b);
    printf("C = %.2f, D = %.2f\n", c, d);
    printf("A = %.3f, B = %.3f\n", a, b);
    printf("C = %.3f, D = %.3f\n", c, d);
    printf("A = %.3E, B = %.3E\n", a, b);
    printf("C = %.3E, D = %.3E\n", c, d);
    printf("A = %.0f, B = %.0f\n", a, b);
    printf("C = %.0f, D = %.0f\n", c, d);

    return 0;
}
