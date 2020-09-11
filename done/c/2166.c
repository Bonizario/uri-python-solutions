#include <stdio.h>

double calcula_raiz(double n)
{
    if (n == 0)
    {
        return 0;
    }
    return 1 / (6 + calcula_raiz(n - 1));
}

int main(void)
{
    int n;

    scanf("%d", &n);

    printf("%.10f\n", 1 + calcula_raiz(n));

    return 0;
}

/* ITERATIVE FORM
 * #include <stdio.h>
 *
 * int main(void)
 * {
 *     int n;
 *     double raiz = 0;
 *
 *     scanf("%d", &n);
 *
 *     while (n--)
 *     {
 *         raiz = 1 / (2 + raiz);
 *     }
 *
 *     printf("%.10f\n", 1 + raiz);
 *
 *     return 0;
 * }
 */
