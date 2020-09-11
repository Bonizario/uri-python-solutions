#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void conversor(int n, int resto, char *s)
{
    while (n > 0)
    {
        resto = n % 2;
        n /= 2;
        if (resto) *s = 'o';
        s++;
    }
}

int main(void)
{
    int horas, minutos, resto;
    char horario[6], s[7], *h, *m;

    while (scanf("%s", horario) != EOF)
    {
        h = strtok(horario, ":");
        m = strtok(NULL, ":");
        horas = atoi(h), minutos = atoi(m);

        memset(s, ' ', 6);
        conversor(horas, resto, s);

        printf(" ____________________________________________\n");
        printf("|                                            |\n");
        printf("|    ____________________________________    |_\n");
        printf("|   |                                    |   |_)\n");
        printf("|   |   8         4         2         1  |   |\n");
        printf("|   |                                    |   |\n");
        printf("|   |   %c         %c         %c         %c  |   |\n",
               s[3], s[2], s[1], s[0]);

        memset(s, ' ', 6);
        conversor(minutos, resto, s);

        printf("|   |                                    |   |\n");
        printf("|   |                                    |   |\n");
        printf("|   |   %c     %c     %c     %c     %c     %c  |   |\n",
               s[5], s[4], s[3], s[2], s[1], s[0]);

        printf("|   |                                    |   |\n");
        printf("|   |   32    16    8     4     2     1  |   |_\n");
        printf("|   |____________________________________|   |_)\n");
        printf("|                                            |\n");
        printf("|____________________________________________|\n\n");
    }

    return 0;
}
