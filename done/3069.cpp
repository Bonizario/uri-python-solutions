// 3069 - Sorvete
#include <cstdio>
#include <algorithm>
#define MAX_SORVETEIROS 10001

struct Intervalo {
    int inicio, fim;
};

bool compara(Intervalo intervalo1, Intervalo intervalo2) {
    return intervalo1.inicio < intervalo2.inicio;
}

int main() {
    struct Intervalo sorveteiros[MAX_SORVETEIROS];
    int i, P, S, min, max, teste = 1;

    while (true) {
        scanf("%d %d", &P, &S);
        if (P == 0 && S == 0)
            break;

        for (i = 0; i < S; i++)
            scanf("%d %d", &sorveteiros[i].inicio, &sorveteiros[i].fim);

        std::sort(sorveteiros, sorveteiros + S, compara);

        min = sorveteiros[0].inicio;
        max = sorveteiros[0].fim;

        printf("Teste %d\n", teste++);
        for (i = 1; i < S; i++) {
            if (sorveteiros[i].inicio > max) {
                printf("%d %d\n", min, max);
                min = sorveteiros[i].inicio;
                max = sorveteiros[i].fim;
            }
            else if (sorveteiros[i].fim > max)
                max = sorveteiros[i].fim;
        }
        printf("%d %d\n\n", min, max);
    }
    return 0;
}
