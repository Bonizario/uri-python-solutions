# 1066 - Even, Odd, Positive and Negative
even_numbers = 0
odd_numbers = 0
positive_numbers = 0
negative_numbers = 0
for _ in range(5):
    n = int(input())
    if (n % 2 == 0):
        even_numbers += 1
    if (n > 0):
        positive_numbers += 1
    elif (n < 0):
        negative_numbers += 1
    odd_numbers = 5 - even_numbers

print("{} valor(es) par(es)".format(even_numbers))
print("{} valor(es) impar(es)".format(odd_numbers))
print("{} valor(es) positivo(s)".format(positive_numbers))
print("{} valor(es) negativo(s)".format(negative_numbers))
