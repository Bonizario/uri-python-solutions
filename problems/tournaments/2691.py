# 2691 - O Matemático
for _ in range(int(input())):
    x, y = map(int, input().split('x'))
    if x != y:
        for i in range(5, 11):
            print('{} x {} = {} && {} x {} = {}'.format(x, i, x * i, y, i, y * i))
    else:
         for i in range(5, 11):
            print('{} x {} = {}'.format(x, i, x * i))

# Solution developed by Lucas Ferreira (BALSAQUE)
# for _ in range( int(input()) ):
#     numeros = list(map( int,input().split("x") ))

#     if len(set(numeros))==1:
#         numeros = numeros[:-1]

#     for i in range(5,10+1):
#         print( " && ".join([ str(numero)+" x "+str(i)+" = "+str(numero*i) for numero in numeros ]) )
