#include <stdio.h>
#include <math.h>

int main(void)
{
    double x1, y1, x2, y2;
    scanf("%lf %lf %lf %lf", &x1, &y1, &x2, &y2);
    double a = x1 - x2, b = y1 - y2;
    double distancia = sqrt(a * a + b * b);
    printf("%.4lf\n", distancia);

    return 0;
}
