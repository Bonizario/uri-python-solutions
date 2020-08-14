#include <stdio.h>

int main(void)
{
    const double pi = 3.14159;
    double raio, volume;

    scanf("%lf", &raio);

    volume = 4 / 3.0 * pi * raio * raio * raio;

    printf("VOLUME = %.3lf\n", volume);

    return 0;
}
