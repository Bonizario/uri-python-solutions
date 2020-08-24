#include <stdio.h>

int main(void)
{
    int x;
    double y;
    scanf("%d %lf", &x, &y);
    printf("%.3lf km/l\n", (double) x / y);

    return 0;
}
