#include <stdio.h>

int main()
{
    double a, b;
    a = 234.345, b = 45.698;
    printf("%.6lf - %.6lf\n", a, b);
    printf("%.0lf - %.0lf\n", a, b);
    printf("%.1lf - %.1lf\n", a, b);
    printf("%.2lf - %.2lf\n", a, b);
    printf("%.3lf - %.3lf\n", a, b);
    printf("%e - %e\n", a, b);
    printf("%E - %E\n", a, b);
    printf("%g - %g\n", a, b);
    printf("%G - %G\n", a, b);

    return 0;
}
