#include <stdio.h>
#include <string.h>

int main(void)
{
    int i, t, n;
    char str[6];

    scanf("%d", &t);

    while (t--)
    {
        scanf("%s", str);
        n = strlen(str);

        if (n == 3)
        {
            if ((str[0] == 'o' &&
                (str[1] == 'n' || str[2] == 'e')) ||
                (str[1] == 'n' && str[2] == 'e'))
                puts("1");
            else
                puts("2");
        }
        else
        {
            puts("3");
        }
    }

    return 0;
}
