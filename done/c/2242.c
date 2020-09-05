#include <stdio.h>
#include <string.h>

int main(void)
{
    char risada[51], vogais[51];

    scanf("%s", risada);

    int i, n, engracada = 1, L = 0, R = 0;

    for (i = 0, n = strlen(risada); i < n; i++)
    {
        char c = risada[i];
        if (c == 'a' || c == 'e' ||
            c == 'i' || c == 'o' || c == 'u')
        {
            vogais[R++] = c;
        }
    }

    R--;

    while (L < R)
    {
        if (vogais[L] != vogais[R])
        {
            engracada = 0;
            break;
        }
        L++, R--;
    }

    printf("%c\n", (engracada ? 'S' : 'N'));

    return 0;
}
