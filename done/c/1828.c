#include <stdio.h>
#include <string.h>

int main(void)
{
    int i, t, caso = 1, n;
    scanf("%d", &t);
    char sheldon[8], raj[8];

    while (t--)
    {
        scanf("%s %s", sheldon, raj);

        if (strcmp(sheldon, raj) == 0)
        {
            printf("Caso #%d: De novo!\n", caso);
        }
        else if (strcmp(sheldon, "tesoura") == 0)
        {
            if ((strcmp(raj, "papel") == 0) || (strcmp(raj, "lagarto") == 0))
                printf("Caso #%d: Bazinga!\n", caso);
            else
                printf("Caso #%d: Raj trapaceou!\n", caso);
        }
        else if (strcmp(sheldon, "papel") == 0)
        {
            if ((strcmp(raj, "pedra") == 0) || (strcmp(raj, "Spock") == 0))
                printf("Caso #%d: Bazinga!\n", caso);
            else
                printf("Caso #%d: Raj trapaceou!\n", caso);
        }
        else if (strcmp(sheldon, "pedra") == 0)
        {
            if ((strcmp(raj, "lagarto") == 0) || (strcmp(raj, "tesoura") == 0))
                printf("Caso #%d: Bazinga!\n", caso);
            else
                printf("Caso #%d: Raj trapaceou!\n", caso);
        }
        else if (strcmp(sheldon, "lagarto") == 0)
        {
            if ((strcmp(raj, "Spock") == 0) || (strcmp(raj, "papel") == 0))
                printf("Caso #%d: Bazinga!\n", caso);
            else
                printf("Caso #%d: Raj trapaceou!\n", caso);
        }
        else
        {
            if ((strcmp(raj, "tesoura") == 0) || (strcmp(raj, "pedra") == 0))
                printf("Caso #%d: Bazinga!\n", caso);
            else
                printf("Caso #%d: Raj trapaceou!\n", caso);
        }
        caso++;
    }

    return 0;
}
