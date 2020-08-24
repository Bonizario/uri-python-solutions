#include <stdio.h>
#include <math.h>

int main(void)
{
    int R;
    scanf("%d", &R);
    double sum = pow(3.0, (double) R);
    printf("%lu\n", (long unsigned) sum);

    return 0;
}
