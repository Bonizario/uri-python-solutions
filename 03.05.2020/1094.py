# 1094 -  Experiments
N = int(input())
rabbits = 0
rats = 0
frogs = 0
for _ in range(N):
    animal = input().strip()
    if (animal[-1] == 'C'):
        rabbits += int(animal[:-2])
    elif (animal[-1] == 'R'):
        rats += int(animal[:-2])
    elif (animal[-1] == 'S'):
        frogs += int(animal[:-2])

total = rabbits + rats + frogs
rabbits_percentage = rabbits / total * 100
rats_percentage = rats / total * 100
frogs_percentage = frogs / total * 100
print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(rabbits))
print("Total de ratos: {}".format(rats))
print("Total de sapos: {}".format(frogs))
print("Percentual de coelhos: {:.2f} %".format(rabbits_percentage))
print("Percentual de ratos: {:.2f} %".format(rats_percentage))
print("Percentual de sapos: {:.2f} %".format(frogs_percentage))
