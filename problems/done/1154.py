# 1154 - Ages
result = 0
counter = 0
age = int(input())
while age >= 0:
    result += age
    counter += 1
    age = int(input())

result = result / counter
print('{:.2f}'.format(result))
