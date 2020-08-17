#include <stdio.h>

int main(void)
{
    int hora_inicial, hora_final;
    scanf("%d%d", &hora_inicial, &hora_final);
    int horas = hora_final - hora_inicial;

    if (horas > 0)
    {
        printf("O JOGO DUROU %d HORA(S)\n", horas);
    }
    else if (horas == 0)
    {
        printf("O JOGO DUROU 24 HORA(S)\n");
    }
    else
    {
        printf("O JOGO DUROU %d HORA(S)\n", 24 + horas);
    }

    return 0;
}
