# 1021 - Banknotes and Coins
N = float(input())
M = int(N)

notas100 = M//100
resto100 = M%100

notas50 = resto100//50
resto50 = resto100%50

notas20 = resto50//20
resto20 = resto50%20

notas10 = resto20//10
resto10 = resto20%10

notas5 = resto10//5
resto5 = resto10%5

notas2 = resto5//2
resto2 = resto5%2

moedas50_cents = int((N - M)/0.5)
resto50_cents = (N - M)%0.5

moedas25_cents = int(resto50_cents/0.25)
resto25_cents = resto50_cents%0.25

moedas10_cents = int(resto25_cents/0.10)
resto10_cents = resto25_cents%0.10

moedas5_cents = int(resto10_cents/0.05)
resto5_cents = resto10_cents%0.05

moedas1_cent = resto5_cents*100

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(notas100))
print('{} nota(s) de R$ 50.00'.format(notas50))
print('{} nota(s) de R$ 20.00'.format(notas20))
print('{} nota(s) de R$ 10.00'.format(notas10))
print('{} nota(s) de R$ 5.00'.format(notas5))
print('{} nota(s) de R$ 2.00'.format(notas2))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(resto2))
print('{} moeda(s) de R$ 0.50'.format(moedas50_cents))
print('{} moeda(s) de R$ 0.25'.format(moedas25_cents))
print('{} moeda(s) de R$ 0.10'.format(moedas10_cents))
print('{} moeda(s) de R$ 0.05'.format(moedas5_cents))
print('{:.0f} moeda(s) de R$ 0.01'.format(moedas1_cent))
