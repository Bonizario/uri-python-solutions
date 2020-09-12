#include <stdio.h>
#include <locale.h>

int eh_primo(int);

int main(void)
{
    // setlocale(LC_ALL, "Portuguese");
    int i, v, m, pulo, moedas[20];
    char vitoria[] = "You’re a coastal aircraft, Robbie, a large silver aircraft.";
    char derrota[] = "Bad boy! I’ll hit you.";

    while (scanf("%d", &m) != EOF)
    {
        v = 0;
        for (i = 0; i < m; i++)
        {
            scanf("%d", &moedas[i]);
        }

        scanf("%d", &pulo);

        for (i = m - 1; i >= 0; i -= pulo)
        {
            v += moedas[i];
        }

        if (eh_primo(v))
        {
            puts(vitoria);
        }
        else
        {
            puts(derrota);
        }
    }

    return 0;
}

int eh_primo(int n) {
	if (n <= 1) return 0;
    else if (n <= 3) return 1;
    else if (n % 2 == 0 || n % 3 == 0) return 0;
    int i = 5;
    while (i * i <= n) {
		if (n % i == 0 || n % (i + 2) == 0) return 0;
        i += 6;
	}
    return 1;
}
