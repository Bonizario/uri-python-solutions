#include <stdio.h>

int main(void)
{
    char uri[] = "AMO FAZER EXERCICIO NO URI";
    printf("<%s>\n", uri);
    printf("<%30s>\n", uri);
    printf("<%.20s>\n", uri);
    printf("<%-20s>\n", uri);
    printf("<%-30s>\n", uri);
    printf("<%.30s>\n", uri);
    printf("<%30.20s>\n", uri);
    printf("<%-30.20s>\n", uri);

    return 0;
}
