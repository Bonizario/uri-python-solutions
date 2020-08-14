#include <stdio.h>

int main(void)
{
    char vendedor[1000];
    double salario, vendas;

    scanf("%s %lf %lf", vendedor, &salario, &vendas);

    salario += 0.15 * vendas;

    printf("TOTAL = R$ %.2lf\n", salario);

    return 0;
}
