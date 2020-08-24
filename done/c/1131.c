#include <stdio.h>

int main(void)
{
    int inter, gremio, novo_grenal, placar[3] = {0, 0, 0};

    do
    {
        scanf("%d %d", &inter, &gremio);

        if (inter > gremio)
        {
            placar[0]++;
        }
        else if (inter < gremio)
        {
            placar[1]++;
        }
        else
        {
            placar[2]++;
        }

        printf("Novo grenal (1-sim 2-nao)\n");
        scanf("%d", &novo_grenal);
    }
    while(novo_grenal == 1);

    printf("%d grenais\n", placar[0] + placar[1] + placar[2]);

    printf("Inter:%d\nGremio:%d\nEmpates:%d\n", placar[0], placar[1], placar[2]);

    if (placar[0] == placar[1])
    {
        printf("Nao houve vencedor\n");
    }
    else if (placar[0] > placar[1])
    {
        printf("Inter venceu mais\n");
    }
    else
    {
        printf("Gremio venceu mais\n");
    }

    return 0;
}
