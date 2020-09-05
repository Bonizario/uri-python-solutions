#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    char str[52];
    int i, n;

    while (fgets(str, 52, stdin) != NULL)
    {
        for (i = 0, n = strlen(str); i < n; i++)
        {
            char c = str[i];
            str[i] = isalpha(c) ? (tolower(c) < 'n' ? (c + 13) : (c - 13)) : c;
        }
        str[i] = '\0';
        printf("%s", str);
    }

    return 0;
}
