#include <stdio.h>
#include <string.h>

int main(void)
{
    int i, t, n;
    scanf("%d", &t);

    char str[6];
    while (t--)
    {
        scanf("%s", str);

        n = strlen(str);
        if (n == 3)
        {
            if ((str[0] == 'o' &&
                (str[1] == 'n' || str[2] == 'e')) ||
                (str[1] == 'n' && str[2] == 'e'))
                printf("1\n");
            else
                printf("2\n");
        }
        else
        {
            printf("3\n");
        }
    }

    return 0;
}
