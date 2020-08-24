#include <stdio.h>

int main(void)
{
    int min_inicial, hora_inicial, min_final, hora_final;

    scanf("%d %d %d %d", &hora_inicial, &min_inicial, &hora_final, &min_final);

    int minutos = min_final - min_inicial;
    int horas = hora_final - hora_inicial;

    if (minutos > 0 && horas == 0)
    {
        horas = 0;
    }
    else if ((minutos > 0 && horas < 0) || (minutos <= 0 && horas <= 0))
    {
        horas += 24;
    }

    if (minutos < 0)
    {
        minutos += 60, horas -= 1;
    }

    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", horas, minutos);

    return 0;
}
