#include <stdio.h>

int main()
{
    int i;
    for (i = 97; i < 123; i++)
    {
        printf("%d e %c\n", i, (char) i);
    }

    return 0;
}
