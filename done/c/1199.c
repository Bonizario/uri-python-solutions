#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *num = (char *) malloc(12 * sizeof(char));

    while (1)
    {
        scanf("%s", num);

        if (num[0] == '-')
        {
            break;
        }
        if (num[1] == 'x')
        {
            printf("%ld\n", strtol(num + 2, NULL, 16));
        }
        else
        {
            printf("0x%X\n", atoi(num));
        }
    }

    free(num);

    return 0;
}
