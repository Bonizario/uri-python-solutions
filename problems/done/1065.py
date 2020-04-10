# 1065 - Even Between five Numbers
even_numbers = 0
for _ in range(5):
    n = int(input())
    if (n % 2 == 0):
        even_numbers += 1
print("{} valores pares".format(even_numbers))
