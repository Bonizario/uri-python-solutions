#include <stdio.h>

int main(void)
{
    int numero, horas;
    double salario_por_hora;

    scanf("%d %d %lf", &numero, &horas, &salario_por_hora);
    double salario = horas * salario_por_hora;

    printf("NUMBER = %d\nSALARY = U$ %.2lf\n", numero, salario);

    return 0;
}
