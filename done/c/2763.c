#include <stdio.h>

int main(void)
{
    char cpf[15];
    scanf("%s", cpf);

    cpf[3] = '\n', cpf[7] = '\n', cpf[11] = '\n', cpf[14] = '\0';

    printf("%s\n", cpf);

    return 0;
}
