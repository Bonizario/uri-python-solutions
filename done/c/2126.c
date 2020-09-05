#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    int caso = 1, qtde;
    char subseq[100], seq[200], *pos, *ultima_pos;

    while (scanf("%s\n", subseq) != EOF)
    {
        scanf("%s", seq);

        pos = seq, ultima_pos = NULL, qtde = 0;

        while (1)
        {
            pos = strstr(pos, subseq);
            if (pos == NULL)
                break;
            ultima_pos = pos;
            qtde++, pos++;
        }

        printf("Caso #%d:\n", caso++);
        if (qtde)
        {
            printf("Qtd.Subsequencias: %d\n", qtde);
            printf("Pos: %ld\n", ultima_pos - seq + 1);
        }
        else
        {
            printf("Nao existe subsequencia\n");
        }
        putchar('\n');
    }

    return 0;
}
