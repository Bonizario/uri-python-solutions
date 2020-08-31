#include <stdio.h>

const int fuso_horario = 6, relacao = 240;

int main(void)
{
    double graus;
    int segundos, minutos, horas;

    while (scanf("%lf", &graus) != EOF)
    {
        int total_segundos = (int) (graus * relacao);
        int horas = (total_segundos / 3600 + fuso_horario) % 24;
        int minutos = (total_segundos / 60) % 60;
        int segundos = (total_segundos % 3600) % 60;

        if (horas >= 0 && horas < 6)
        {
            printf("De Madrugada!!\n");
        }
        else if (horas >= 6 && horas < 12)
        {
            printf("Bom Dia!!\n");
        }
        else if (horas >= 12 && horas < 18)
        {
            printf("Boa Tarde!!\n");
        }
        else
        {
            printf("Boa Noite!!\n");
        }
        printf("%02d:%02d:%02d\n", horas, minutos, segundos);
    }

    return 0;
}


/*
// A cada 24h, temos 86400 segundos
// A cada 24h, temos 360 graus
// -----------------------------------------
// Relacao:
// 360 graus - 86400 s
// 1 grau - 240 s
// -----------------------------------------
// Existe um fuso horario de 6h:
// 0 graus: 6h00 (21600s)
// 90 graus: 12h00 (43200s)
// 180 graus: 18h00 (64800s)
// 270 graus: 0h00 (0s)

#include <stdio.h>

const int fuso_horario = 6, relacao = 240;

int main(void)
{
    double graus;
    int segundos, minutos, horas;

    while (scanf("%lf", &graus) != EOF)
    {
        // (int) (graus * relacao)                       => quantidade total inteira de segundos
        // (int) (graus * relacao) / 3600                => quantidade total de horas
        // (int) (graus * relacao) / 3600 + fuso_horario => quantidade total de horas ajustada com o fuso horario
        // % 24 => apenas para converter 24h para 0h, qualquer valor no intervalo [0, 23] continua igual
        int horas = ((int) (graus * relacao) / 3600 + fuso_horario) % 24;


        // (int) (graus * relacao) / 60 + fuso_horario * 60        => quantidade total inteira de minutos
        // ((int) (graus * relacao) / 60 + fuso_horario * 60) % 60 => quantidade "efetiva" de minutos
        // Exemplo: 95 graus = 740 minutos; 740 % 60 = 20 minutos; (720 minutos foram aproveitados como 12h)
        // Obs: adicionar (fuso_horario * 60) nao altera o resultado, pois faremos % 60 posteriormente
        // Simplificando: ((int) (graus * relacao) / 60) % 60      => quantidade "efetiva" de minutos
        int minutos = ((int) (graus * relacao) / 60) % 60;


        // (int) (graus * relacao)               => quantidade total inteira de segundos
        // (int) (graus * relacao) % 3600        => quantidade de segundos restantes: 85000 % 3600 = 2200
        // ((int) (graus * relacao) % 3600) % 60 => quantidade efetiva de segundos: 2200 % 60 = 40
        int segundos = ((int) (graus * relacao) % 3600) % 60;


        if (horas >= 0 && horas < 6)
        {
            printf("De Madrugada!!\n");
        }
        else if (horas >= 6 && horas < 12)
        {
            printf("Bom Dia!!\n");
        }
        else if (horas >= 12 && horas < 18)
        {
            printf("Boa Tarde!!\n");
        }
        else
        {
            printf("Boa Noite!!\n");
        }
        printf("%02d:%02d:%02d\n", horas, minutos, segundos);
    }

    return 0;
}
*/
