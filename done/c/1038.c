#include <stdio.h>

int main(void)
{
    int codigo, quantidade;
    scanf("%d%d", &codigo, &quantidade);

    float total = 0;
    switch (codigo)
    {
        case 1:
            total += quantidade * 4.0;
            break;
        case 2:
            total += quantidade * 4.50;
            break;
        case 3:
            total += quantidade * 5.0;
            break;
        case 4:
            total += quantidade * 2.0;
            break;
        case 5:
            total += quantidade * 1.5;
            break;
    }
    printf("Total: R$ %.2f\n", total);

    return 0;
}
