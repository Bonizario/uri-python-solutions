#include <stdio.h>
#include <string.h>

int main(void)
{
    char s1[13], s2[9], s3[11];
    scanf("%s %s %s", s1, s2, s3);

    if (strcmp(s1, "vertebrado") == 0)
    {
        if (strcmp(s2, "ave") == 0)
        {
            if (strcmp(s3, "carnivoro") == 0)
                printf("aguia\n");
            else
                printf("pomba\n");
        }
        else
        {
            if (strcmp(s3, "onivoro") == 0)
                printf("homem\n");
            else
                printf("vaca\n");
        }
    }
    else
    {
        if (strcmp(s2, "inseto") == 0)
        {
            if (strcmp(s3, "hematofago") == 0)
                printf("pulga\n");
            else
                printf("lagarta\n");
        }
        else
        {
            if (strcmp(s3, "hematofago") == 0)
                printf("sanguessuga\n");
            else
                printf("minhoca\n");
        }
    }

    return 0;
}
