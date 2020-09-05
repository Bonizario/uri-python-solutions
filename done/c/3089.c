/**
 * #include <stdlib.h>
 * http://www.cplusplus.com/reference/cstdlib/qsort/
 *
 * const void * because we can sort different types of data
 * e.g.: structs, floats, doubles, not just int
 *
 * void qsort (void* base, size_t num, size_t size,
            int (*compar)(const void*,const void*));
 *
 * < 0:  [a, b]
 * == 0: [a, b] (qsort is stable)
 * > 0:  [b, a]
 *
 * int cmp(const void *a, const void *b)
 * {
      return (*(int*) a - *(int*) b);
 * }
 */

#include <stdio.h>

int main(void)
{
    int i, j, n, par, caro, barato, nums[20000];

    while (scanf("%d", &n))
    {
        if (n == 0)
            break;

        j = n * 2;
        for (i = 0; i < j; i++)
            scanf("%d", &nums[i]);

        i = 0, j -= 1, caro = nums[j], barato = 2 * nums[0];

        while (n--)
        {
            par = nums[i++] + nums[j--];
            if (caro < par)
                caro = par;
            if (barato > par)
                barato = par;
        }
        printf("%d %d\n", caro, barato);
    }

    return 0;
}
