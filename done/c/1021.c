#include <stdio.h>

int main(void)
{
    int notas, moedas;
    scanf("%d.%d", &notas, &moedas);

    printf("NOTAS:\n");
    printf("%d nota(s) de R$ 100.00\n", notas / 100);
    notas %= 100;
    printf("%d nota(s) de R$ 50.00\n", notas / 50);
    notas %= 50;
    printf("%d nota(s) de R$ 20.00\n", notas / 20);
    notas %= 20;
    printf("%d nota(s) de R$ 10.00\n", notas / 10);
    notas %= 10;
    printf("%d nota(s) de R$ 5.00\n", notas / 5);
    notas %= 5;
    printf("%d nota(s) de R$ 2.00\n", notas / 2);
    notas %= 2;

    printf("MOEDAS:\n");
    printf("%d moeda(s) de R$ 1.00\n", notas);
    printf("%d moeda(s) de R$ 0.50\n", moedas / 50);
    moedas %= 50;
    printf("%d moeda(s) de R$ 0.25\n", moedas / 25);
    moedas %= 25;
    printf("%d moeda(s) de R$ 0.10\n", moedas / 10);
    moedas %= 10;
    printf("%d moeda(s) de R$ 0.05\n", moedas / 5);
    moedas %= 5;
    printf("%d moeda(s) de R$ 0.01\n", moedas);

    return 0;
}
